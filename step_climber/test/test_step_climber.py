import unittest

from src.step_climber import Stair, Climber, StairTooShortException


class TestClimber(unittest.TestCase):

    def test_climb_no_path(self):

        ladder = Stair(7)

        hiker = Climber(steps_allowed=(2, 4))
        self.assertEqual(0, hiker.path_count)
        hiker.start_climbing(stair=ladder)

        self.assertEqual(0, hiker.path_count)

    def test_climb_one_path(self):

        ladder = Stair(14)

        hiker = Climber(steps_allowed=(7, ))

        hiker.start_climbing(stair=ladder)

        self.assertEqual(1, hiker.path_count)

    def test_climb_many_paths(self):

        ladder = Stair(12)

        hiker = Climber(steps_allowed=(2, 3, 4))

        hiker.start_climbing(stair=ladder)

        self.assertEqual(36, hiker.path_count)

    def test_stair_too_short(self):

        ladder = Stair(0)

        self.assertRaises(StairTooShortException)
