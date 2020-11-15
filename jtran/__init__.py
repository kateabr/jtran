"""
Functions for easy transliteration of kana from/to latin.

Much of the work here is inspired/inherited/etc from Kim Ahlström and his work on "Ve", built in Ruby.

Credit where credit is due:
https://github.com/Kimtaro/ve/blob/master/lib/providers/japanese_transliterators.rb
"""
__author__ = """Ekaterina Biryukova"""
__email__ = "kateabr@yandex.ru"
__version__ = "0.1.0"

from .jtran import JTran

__all__ = ["JTran"]
