import unittest

from jtran import JTran


class TestJtran(unittest.TestCase):
    def test_jtran(self):
        self.assertEqual(JTran.transliterate_from_latn_to_hrkt("kanazawa"), "かなざわ")
        self.assertEqual(JTran.transliterate_from_hira_to_latn("かなざわ"), "kanazawa")
        self.assertEqual(
            JTran.transliterate_from_hrkt_to_latn("(ストロベリー)"), "(storoberi-)"
        )

        self.assertEqual(JTran.transliterate_from_kana_to_hira("キットカート"), "きっとかーと")
        self.assertEqual(JTran.transliterate_from_hira_to_kana("かなざわ"), "カナザワ")

        # self.assertEqual(JTran.transliterate_from_halfwidth_to_fullwidth(''), "")
        # self.assertEqual(JTran.transliterate_from_fullwidth_to_halfwidth(''), "")
