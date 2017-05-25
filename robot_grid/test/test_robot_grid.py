import unittest

from robot_grid.src.robot_grid import Grid


class TestTraverseGrid(unittest.TestCase):

    def test_traverse_grid_minimal(self):

        grid_count_paths = Grid()

        grid_count_paths.traverse_grid(1, 1)

        self.assertEqual(grid_count_paths.count, 2)

    def test_traverse_grid_more_complex(self):

        grid_count_paths = Grid()

        grid_count_paths.traverse_grid(2, 2)

        self.assertEqual(grid_count_paths.count, 6)

    def test_traverse_grid_minimal_one_blocker(self):

        grid_count_paths = Grid(blocks=[(1, 0)])

        grid_count_paths.traverse_grid(1, 1)

        self.assertEqual(grid_count_paths.count, 1)

    def test_traverse_grid_more_comples_two_blocks(self):

        grid_count_paths = Grid(blocks=[(2, 1), (1, 1)])

        grid_count_paths.traverse_grid(2, 2)

        self.assertEqual(grid_count_paths.count, 1)
