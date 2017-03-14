import unittest
from anagram_counter import find_anagrams

class TestAnagrams(unittest.TestCase):

    def test_find_anagrams(self):

        # fixture

        word_list = ["mare", "rema", "canto", "conta", "calendario", "locandiera"]

        anagram_groups = find_anagrams(word_list)

        self.assertListEqual(anagram_groups,
                             sorted([["mare", "rema"], ["canto", "conta"], ["calendario", "locandiera"]]))
