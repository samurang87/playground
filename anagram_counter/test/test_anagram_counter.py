import unittest
from src.anagram_counter import find_anagrams


class TestAnagrams(unittest.TestCase):

    def test_find_anagrams(self):

        # fixture

        word_list = ["mare", "rema", "mare", "canto", "conta", "calendario", "locandiera", "pulcino"]

        # execution

        anagram_groups = find_anagrams(word_list)

        # check

        self.assertListEqual(sorted(anagram_groups),
                             sorted([["mare", "rema"], ["canto", "conta"], ["calendario", "locandiera"]]))
