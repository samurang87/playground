import unittest
from src.anagram_counter import find_anagrams, clean_english


class TestAnagrams(unittest.TestCase):

    def test_find_anagrams(self):

        # fixture

        word_list = ["mare", "rema", "mare", "canto", "conta", "calendario", "locandiera", "pulcino"]

        # execution

        anagram_groups = find_anagrams(word_list)

        # check

        self.assertListEqual(sorted(anagram_groups),
                             sorted([["mare", "rema"], ["canto", "conta"], ["calendario", "locandiera"]]))

    def test_clean_english(self):

        a_string = 'if it$%&/(),\n\'fits I \nsits'

        self.assertListEqual(clean_english(a_string).split(), ['if', 'it', 'fits', 'i', 'sits'])
