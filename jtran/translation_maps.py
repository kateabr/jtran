H_SYLLABIC_N = 'ん'
H_SMALL_TSU = 'っ'

HIRA_TO_LATN = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
    "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "だ": "da", "ぢ": "ji", "づ": "zu", "で": "de", "ど": "do",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
    "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
    "や": "ya", "ゆ": "y", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
    "わ": "wa", "うぃ": "whi", "うぇ": "whe", "を": "wo",
    "ゑ": "wye", "ゐ": "wyi", "ー": ":", "ん": "n",

    "きゃ": "kya", "きゅ": "ky", "きょ": "kyo", "きぇ": "kye", "きぃ": "kyi",
    "ぎゃ": "gya", "ぎゅ": "gy", "ぎょ": "gyo", "ぎぇ": "gye", "ぎぃ": "gyi",
    "くぁ": "kwa", "くぃ": "kwi", "くぅ": "kw", "くぇ": "kwe", "くぉ": "kwo",
    "ぐぁ": "qwa", "ぐぃ": "gwi", "ぐぅ": "gw", "ぐぇ": "gwe", "ぐぉ": "gwo",
    "しゃ": "sha", "しぃ": "syi", "しゅ": "sh", "しぇ": "she", "しょ": "sho",
    "じゃ": "jya", "じゅ": "zy", "じぇ": "zye", "じょ": "zyo", "じぃ": "zyi",
    "すぁ": "swa", "すぃ": "swi", "すぅ": "sw", "すぇ": "swe", "すぉ": "swo",
    "ちゃ": "tya", "ちゅ": "ty", "ちぇ": "tye", "ちょ": "tyo", "ちぃ": "tyi",
    "ぢゃ": "dya", "ぢぃ": "dyi", "ぢゅ": "dy", "ぢぇ": "dye", "ぢょ": "dyo",
    "つぁ": "tsa", "つぃ": "tsi", "つぇ": "tse", "つぉ": "tso", "てゃ": "tha",
    "てぃ": "thi", "てゅ": "th", "てぇ": "the", "てょ": "tho", "とぁ": "twa",
    "とぃ": "twi", "とぅ": "tw", "とぇ": "twe", "とぉ": "two", "でゃ": "dha",
    "でぃ": "dhi", "でゅ": "dh", "でぇ": "dhe", "でょ": "dho", "どぁ": "dwa",
    "どぃ": "dwi", "どぅ": "dw", "どぇ": "dwe", "どぉ": "dwo", "にゃ": "nya",
    "にゅ": "ny", "にょ": "nyo", "にぇ": "nye", "にぃ": "nyi", "ひゃ": "hya",
    "ひぃ": "hyi", "ひゅ": "hy", "ひぇ": "hye", "ひょ": "hyo", "びゃ": "bya",
    "びぃ": "byi", "びゅ": "by", "びぇ": "bye", "びょ": "byo", "ぴゃ": "pya",
    "ぴぃ": "pyi", "ぴゅ": "py", "ぴぇ": "pye", "ぴょ": "pyo", "ふぁ": "fwa",
    "ふぃ": "fyi", "ふぇ": "fye", "ふぉ": "fwo", "ふぅ": "fw", "ふゃ": "fya",
    "ふゅ": "fy", "ふょ": "fyo", "みゃ": "mya", "みぃ": "myi", "みゅ": "my",
    "みぇ": "mye", "みょ": "myo", "りゃ": "rya", "りぃ": "ryi", "りゅ": "ry",
    "りぇ": "rye", "りょ": "ryo",
    "ゔぁ": "va", "ゔぃ": "vyi", "ゔ": "v", "ゔぇ": "vye", "ゔぉ": "vo",
    "ゔゃ": "vya", "ゔゅ": "vy", "ゔょ": "vyo",
    "うぁ": "wha", "いぇ": "ye", "うぉ": "who",
    "ぁ": "xa", "ぃ": "xi", "ぅ": "x", "ぇ": "xe", "ぉ": "xo",
    "ゕ": "xka", "ゖ": "xke", "ゎ": "xwa", "々": "qi"
}

LATN_TO_HIRA = {
    'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お',
    'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
    'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
    'sa': 'さ', 'si': 'し', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
    'za': 'ざ', 'zi': 'じ', 'ji': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
    'ta': 'た', 'ti': 'ち', 'chi': 'ち', 'tu': 'つ', 'tsu': 'つ', 'te': 'て', 'to': 'と',
    'da': 'だ', 'di': 'ぢ', 'du': 'づ', 'dzu': 'づ', 'de': 'で', 'do': 'ど',
    'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
    'ha': 'は', 'hi': 'ひ', 'hu': 'ふ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
    'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
    'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',
    'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
    'ya': 'や', 'yu': 'ゆ', 'yo': 'よ',
    'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
    'la': 'ら', 'li': 'り', 'lu': 'る', 'le': 'れ', 'lo': 'ろ',
    'wa': 'わ', 'wi': 'うぃ', 'we': 'うぇ', 'wo': 'を',
    'wye': 'ゑ', 'wyi': 'ゐ', '-': 'ー', ':': 'ー',

    'n': 'ん', 'm': 'ん', "n'": 'ん',

    'kya': 'きゃ', 'kyu': 'きゅ', 'kyo': 'きょ', 'kye': 'きぇ', 'kyi': 'きぃ',
    'gya': 'ぎゃ', 'gyu': 'ぎゅ', 'gyo': 'ぎょ', 'gye': 'ぎぇ', 'gyi': 'ぎぃ',
    'kwa': 'くぁ', 'kwi': 'くぃ', 'kwu': 'くぅ', 'kwe': 'くぇ', 'kwo': 'くぉ',
    'gwa': 'ぐぁ', 'gwi': 'ぐぃ', 'gwu': 'ぐぅ', 'gwe': 'ぐぇ', 'gwo': 'ぐぉ',

    'sya': 'しゃ', 'syi': 'しぃ', 'syu': 'しゅ', 'sye': 'しぇ', 'syo': 'しょ',
    'sha': 'しゃ', 'shu': 'しゅ', 'she': 'しぇ', 'sho': 'しょ',
    'ja': 'じゃ', 'ju': 'じゅ', 'je': 'じぇ', 'jo': 'じょ',
    'jya': 'じゃ', 'jyi': 'じぃ', 'jyu': 'じゅ', 'jye': 'じぇ', 'jyo': 'じょ',
    'zya': 'じゃ', 'zyu': 'じゅ', 'zyo': 'じょ', 'zye': 'じぇ', 'zyi': 'じぃ',
    'swa': 'すぁ', 'swi': 'すぃ', 'swu': 'すぅ', 'swe': 'すぇ', 'swo': 'すぉ',

    'cha': 'ちゃ', 'chu': 'ちゅ', 'che': 'ちぇ', 'cho': 'ちょ',
    'cya': 'ちゃ', 'cyi': 'ちぃ', 'cyu': 'ちゅ', 'cye': 'ちぇ', 'cyo': 'ちょ',
    'tya': 'ちゃ', 'tyi': 'ちぃ', 'tyu': 'ちゅ', 'tye': 'ちぇ', 'tyo': 'ちょ',
    'dya': 'ぢゃ', 'dyi': 'ぢぃ', 'dyu': 'ぢゅ', 'dye': 'ぢぇ', 'dyo': 'ぢょ',
    'tsa': 'つぁ', 'tsi': 'つぃ', 'tse': 'つぇ', 'tso': 'つぉ',
    'tha': 'てゃ', 'thi': 'てぃ', 'thu': 'てゅ', 'the': 'てぇ', 'tho': 'てょ',
    'twa': 'とぁ', 'twi': 'とぃ', 'twu': 'とぅ', 'twe': 'とぇ', 'two': 'とぉ',
    'dha': 'でゃ', 'dhi': 'でぃ', 'dhu': 'でゅ', 'dhe': 'でぇ', 'dho': 'でょ',
    'dwa': 'どぁ', 'dwi': 'どぃ', 'dwu': 'どぅ', 'dwe': 'どぇ', 'dwo': 'どぉ',

    'nya': 'にゃ', 'nyu': 'にゅ', 'nyo': 'にょ', 'nye': 'にぇ', 'nyi': 'にぃ',

    'hya': 'ひゃ', 'hyi': 'ひぃ', 'hyu': 'ひゅ', 'hye': 'ひぇ', 'hyo': 'ひょ',
    'bya': 'びゃ', 'byi': 'びぃ', 'byu': 'びゅ', 'bye': 'びぇ', 'byo': 'びょ',
    'pya': 'ぴゃ', 'pyi': 'ぴぃ', 'pyu': 'ぴゅ', 'pye': 'ぴぇ', 'pyo': 'ぴょ',
    'fa': 'ふぁ', 'fi': 'ふぃ', 'fe': 'ふぇ', 'fo': 'ふぉ',
    'fwa': 'ふぁ', 'fwi': 'ふぃ', 'fwu': 'ふぅ', 'fwe': 'ふぇ', 'fwo': 'ふぉ',
    'fya': 'ふゃ', 'fyi': 'ふぃ', 'fyu': 'ふゅ', 'fye': 'ふぇ', 'fyo': 'ふょ',

    'mya': 'みゃ', 'myi': 'みぃ', 'myu': 'みゅ', 'mye': 'みぇ', 'myo': 'みょ',

    'rya': 'りゃ', 'ryi': 'りぃ', 'ryu': 'りゅ', 'rye': 'りぇ', 'ryo': 'りょ',
    'lya': 'りゃ', 'lyu': 'りゅ', 'lyo': 'りょ', 'lye': 'りぇ', 'lyi': 'りぃ',

    'va': 'ゔぁ', 'vi': 'ゔぃ', 'vu': 'ゔ', 've': 'ゔぇ', 'vo': 'ゔぉ',
    'vya': 'ゔゃ', 'vyi': 'ゔぃ', 'vyu': 'ゔゅ', 'vye': 'ゔぇ', 'vyo': 'ゔょ',
    'wha': 'うぁ', 'whi': 'うぃ', 'ye': 'いぇ', 'whe': 'うぇ', 'who': 'うぉ',

    'xa': 'ぁ', 'xi': 'ぃ', 'xu': 'ぅ', 'xe': 'ぇ', 'xo': 'ぉ',
    'xya': 'ゃ', 'xyu': 'ゅ', 'xyo': 'ょ',
    'xtu': 'っ', 'xtsu': 'っ',
    'xka': 'ゕ', 'xke': 'ゖ', 'xwa': 'ゎ',

    'k': 'っ', 's': 'っ', 't': 'っ', 'h': 'っ', 'r': 'っ',
    'g': 'っ', 'z': 'っ', 'd': 'っ', 'b': 'っ', 'p': 'っ',
    'qi': '々', '・': ''
}
