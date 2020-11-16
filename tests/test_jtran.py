import unittest

from jtran import JTran


class TestJtran(unittest.TestCase):
    def test_jtran(self):
        self.assertEqual(JTran.transliterate_from_latn_to_hrkt("yako:"), "やこう")
        self.assertEqual(JTran.transliterate_from_latn_to_hrkt("yakou"), "やこう")
        self.assertEqual(
            JTran.transliterate_from_hrkt_to_latn("(ストロベリー)"), "(sutoroberii)"
        )

        self.assertEqual(JTran.transliterate_from_kana_to_hira("キロメートル"), "きろめえとる")
        self.assertEqual(JTran.transliterate_from_kana_to_hira("チューリップ"), "ちゅうりっぷ")

        self.assertEqual(JTran.transliterate_from_kana_to_hira("ストロベリー"), "すとろべりい")

        self.assertEqual(JTran.transliterate_from_kana_to_hira("キットキャット"), "きっときゃっと")
        self.assertEqual(JTran.transliterate_from_hira_to_kana("かなざわ"), "カナザワ")

        self.assertEqual(JTran.transliterate_from_hira_to_latn("ぜんや"), "zen'ya")

        self.assertEqual(JTran.transliterate_from_halfwidth_to_fullwidth("abcde123"), "ａｂｃｄｅ１２３")
        self.assertEqual(JTran.transliterate_from_fullwidth_to_halfwidth("ａｂｃｄｅ１２３"), "abcde123")
