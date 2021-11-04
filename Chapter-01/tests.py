import unittest
import gridy

class TestGridy(unittest.TestCase):

    def test_grid_size(self):
        grid = gridy.Grid(42,13)
        self.assertEqual(grid.width, 42)
        self.assertEqual(grid.height, 13)

    def test_grid_content(self):
        grid = gridy.Grid(42,13)
        count = 0
        for cell in grid:
            count += 1
        self.assertEqual(count, 42*13)


    def test_grid_content(self):
        grid = gridy.Grid(4,3)
        grid_str =  """\
#########
# | | | #
#-+-+-+-#
# | | | #
#-+-+-+-#
# | | | #
#########
"""
        self.assertEqual(repr(grid), grid_str)
        cell = grid[0,0]
        self.assertEqual(cell.n, None)
        self.assertNotEqual(cell.e, None)


    def test_grid_carve(self):
        grid = gridy.Grid(4,3)
        cell = grid[0,0]
        cell.carve_e()
        grid_str =  """\
#########
#   | | #
#-+-+-+-#
# | | | #
#-+-+-+-#
# | | | #
#########
"""
        self.assertEqual(repr(grid), grid_str)


if __name__ == '__main__':
    unittest.main()