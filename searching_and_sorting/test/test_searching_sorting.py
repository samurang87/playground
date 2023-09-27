import unittest

from searching_and_sorting.src.searching_sorting import mergesort, sorted_merge


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


class TestMergeSort(unittest.TestCase):

    def test_merge_sort_ints(self):

        input = [5, 7, 22, 1, 9, 13, 3]

        want = sorted(input)

        mergesort(input, 0, len(input)-1)

        self.assertEqual(want, input)
