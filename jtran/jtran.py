import re

from jtran.translation_maps import H_SYLLABIC_N, H_SMALL_TSU, HIRA_TO_LATN, LATN_TO_HIRA


class JTran:
    @staticmethod
    def remove_colons_from_transliteration(text: str) -> str:
        lvowels = {'a:': 'aa', 'i:': 'ii', 'u:': 'uu', 'e:': 'ee', 'o:': 'ou'}
        return re.sub(r'(\w:)', lambda m: lvowels[m.group(1)] if m.group(1) in lvowels.keys() else m.group(1), text)

    @staticmethod
    def transliterate_from_hrkt_to_latn(text: str) -> str:
        """
        Transliterates from [Hirag/Katak]ana to Latin/En.

        :param text: text to transliterate.
        :return: transliterated text
        """

        text = JTran.transliterate_from_kana_to_hira(text)
        return JTran.remove_colons_from_transliteration(JTran.transliterate_from_hira_to_latn(text))

    @staticmethod
    def transliterate_from_hira_to_latn(text: str) -> str:
        """
        Transliterates from Hiragana to Latin/En. Phonetics, that is.

        :param text text to transliterate
        :return: transliterated text
        """
        # Decode once, not twice
        _H_SMALL_TSU = H_SMALL_TSU
        _H_SYLLABIC_N = H_SYLLABIC_N

        kana = text * 1
        romaji = ""
        geminate = False

        index = 0
        klength = len(kana)

        while klength > 0:
            for length in [2, 1]:
                mora = ""
                for_conversion = kana[index: (index + length)]

                if for_conversion == _H_SMALL_TSU:
                    geminate = True
                    index += length
                    klength -= length
                    break

                elif for_conversion == _H_SYLLABIC_N and re.match("[あいうえおやゆよ]", kana[(index + 1): (index + 2)]):
                    # Syllabic N before open syllables
                    mora = "n'"
                elif for_conversion in HIRA_TO_LATN:
                    mora = HIRA_TO_LATN[for_conversion]

                if len(mora) > 0:
                    if geminate:
                        geminate = False
                        romaji += mora[:1]

                    romaji += mora
                    index += length
                    klength -= length
                    break
                elif length == 1:
                    romaji += for_conversion
                    index += length
                    klength -= length

        return JTran.remove_colons_from_transliteration(romaji)

    @staticmethod
    def transliterate_from_latn_to_hrkt(text: str, colons_to_double_vowel: bool = True) -> str:
        """
        Transliterates from Latin/En to Hiragana (mostly).

        :param text: text to transliterate
        :param colons_to_double_vowel: whether to change colons into another vowel or a vowel length indicator
        :return: transliterated text
        """
        # Duplicate the text...
        romaji = JTran.remove_colons_from_transliteration(text) if colons_to_double_vowel else text * 1
        kana = ""

        romaji = re.sub("/m([BbPp])/", "n\1", romaji)
        romaji = re.sub("/M([BbPp])/", "N\1", romaji)

        index = 0
        rlength = len(romaji) - 1

        while rlength >= 0:
            for for_removal in [3, 2, 1]:
                mora = ""
                for_conversion = romaji[index: (index + for_removal)]
                is_upper = True if re.search("[A-Z][^A-Z]*", for_conversion) else False
                for_conversion = for_conversion.lower()

                if re.match("/nn[aiueo]/", for_conversion):
                    mora = H_SYLLABIC_N
                    for_removal = 1
                elif for_conversion in LATN_TO_HIRA:
                    mora = LATN_TO_HIRA[for_conversion]
                elif for_conversion == "tch" or (
                        for_removal == 2
                        and re.match("/([kgsztdnbpmyrlwc])\1/", for_conversion)
                ):
                    mora = H_SMALL_TSU
                    for_removal = 1

                if mora != "":
                    if is_upper:
                        kana += JTran.transliterate_from_hira_to_kana(text=(mora * 1))
                    else:
                        kana += mora

                    index += for_removal
                    rlength -= for_removal
                    break
                elif for_removal == 1:
                    kana += for_conversion
                    index += 1
                    rlength -= 1

        return kana

    @staticmethod
    def transliterate_from_kana_to_hira(text: str) -> str:
        """
        Transliterates from Katakana to Hiragana.

        :param text text to transliterate
        :return: transliterated text
        """
        if 'ー' not in text:
            return JTran.transpose_codepoints_in_range(text, -96, 12449, 12534)
        return JTran.transliterate_from_latn_to_hrkt(
            JTran.transliterate_from_hira_to_latn(
                JTran.transpose_codepoints_in_range(text, -96, 12449, 12534)))

    @staticmethod
    def transliterate_from_hira_to_kana(text: str) -> str:
        """
        Transliterates from Hiragana to Katakana.

        :param text text to transliterate
        :return: transliterated text
        """
        return JTran.transpose_codepoints_in_range(text, 96, 12353, 12438)

    @staticmethod
    def transliterate_from_fullwidth_to_halfwidth(text: str) -> str:
        """
        Transliterates from full-width to half-width.

        :param text text to transliterate
        :return: transliterated text
        """
        text = JTran.transpose_codepoints_in_range(text, -65248, 65281, 65374)
        return JTran.transpose_codepoints_in_range(text, -12256, 12288, 12288)

    @staticmethod
    def transliterate_from_halfwidth_to_fullwidth(text: str) -> str:
        """
        Transliterates from half-width to full-width.

        :param text text to transliterate
        :return: transliterated text
        """
        text = JTran.transpose_codepoints_in_range(text, 65248, 33, 126)
        return JTran.transpose_codepoints_in_range(text, 12256, 32, 32)

    @staticmethod
    def transpose_codepoints_in_range(
            text: str, distance: int, range_start: int, range_end: int
    ) -> str:
        """
        Given a set of text (unicode...), coupled with distance and range, transposes
        it for a corresponding swap and returns the new set.

        :param text text to be transposed, codepoint-wise
        :param distance to the other side of the map
        :param range_start start of the range we're interested in, codepont-wise
        :param range_end end of the range we're interested in, codepoint-wise

        :return: transposed text
        """

        transposed_text = ""
        codepoints = map(lambda char: ord(char), list(text))

        for codepoint in codepoints:
            if range_start <= codepoint <= range_end:
                transposed_text += chr(codepoint + distance)
            else:
                transposed_text += chr(codepoint)

        return transposed_text
