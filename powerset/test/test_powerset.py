import unittest
import ddt
from src.powerset import powerset


class TestPowerset(unittest.TestCase):

    def test_powerset_empty(self):

        a_set = []

        self.assertListEqual(list(powerset(a_set)), [[]])

    def test_powerset_single(self):

        a_set = [2]

        self.assertListEqual(list(powerset(a_set)), [[], [2]])

    def test_powerset_multiple(self):

        a_set = [1, 2, 3]

        self.assertListEqual(sorted(list(powerset(a_set))),
                             sorted([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]))




