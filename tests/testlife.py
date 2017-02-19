from gameoflife.Life import Life
import unittest

class testLife(unittest.TestCase):

    def grid_to_coords(self, grid):
        """
        Converts a 2D list to a set of coordinates.
        """
        coords = set()
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
              if grid[i][j]:
                  coords.add((i, j))

        return coords

    def test_no_interaction(self):
        emptyState = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        testLife = Life(self.grid_to_coords(emptyState))
        testLife.evolve()
        self.assertEqual(set(), testLife.state)

    def test_cell_death(self):
        """
        Tests that a cell dies if it has less than two neighbours.
        """
        starting_state = [
            [1, 0, 1],
            [0, 1, 1],
            [0, 0, 0]
        ]
        testLife = Life(self.grid_to_coords(starting_state))
        testLife.evolve()
        self.assertEqual(self.grid_to_coords([
            [0, 0, 1],
            [0, 1, 1],
            [0, 0, 0]
        ]), testLife.state)
