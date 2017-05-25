import unittest

from robot_grid.src.robot_grid import GridPaths


class TestTraverseGrid(unittest.TestCase):

    def test_traverse_grid_minimal(self):

        grid_count_paths = GridPaths()

        grid_count_paths.traverse_grid(1, 1)

        self.assertEqual(grid_count_paths.count, 2)

    def test_traverse_grid_more_complex(self):

        grid_count_paths = GridPaths()

        grid_count_paths.traverse_grid(2, 2)

        self.assertEqual(grid_count_paths.count, 6)
