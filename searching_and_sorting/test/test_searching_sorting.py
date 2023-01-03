import unittest

from searching_and_sorting.src.searching_sorting import sorted_merge


class TestSortedMerge(unittest.TestCase):
    def test_sorted_merge_empty_a(self):
        a = []
        b = [1, 2, 3]

        merged = sorted_merge(a, b)

        self.assertEqual([1, 2, 3], merged)

    def test_sorted_merge(self):

        a = [1, 2, 3, 5, 7, 9]
        b = [4, 6, 8]

        merged = sorted_merge(a, b)

        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], merged)
