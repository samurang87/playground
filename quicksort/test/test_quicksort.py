import unittest

from quicksort.src.quicksort import partition, quicksort


class TestQuicksort(unittest.TestCase):

    def test_partition(self):

        input = [4, 5, 3, 7, 2]

        expected = [3, 2, 4, 5, 7]

        left, mid, right = partition(input)

        self.assertListEqual(expected, left+mid+right)

    def test_quicksort_regular_case(self):

        self.assertListEqual(quicksort([5, 8, 1, 3, 7, 9, 2]), [1, 2, 3, 5, 7, 8, 9])

    def test_quicksort_long(self):

        self.assertListEqual(quicksort([233, 3, 68, 243, 12, 83, 222, 22, 191, 12, 394, 12, 33, 411]),
                             [3, 12, 12, 12, 22, 33, 68, 83, 191, 222, 233, 243, 394, 411])
