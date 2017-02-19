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

    def create_evolve_assert(self, initial_state, final_state):
        testLife = Life(self.grid_to_coords(initial_state))
        testLife.evolve()
        self.assertEqual(self.grid_to_coords(final_state), testLife.state)

    def test_no_interaction(self):
        self.create_evolve_assert([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ], [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

    def test_cell_death(self):
        """
        Tests that a cell dies if it has less than two neighbours.
        """
        self.create_evolve_assert([
            [1, 0, 1],
            [0, 1, 1],
            [0, 0, 0]
        ], [
            [0, 0, 1],
            [0, 1, 1],
            [0, 0, 0]
        ])

    def test_death_via_abundance(self):
        """
        Tests that a cell dies if it has more than 3 neighbours.
        """
        self.create_evolve_assert([
            [1, 1, 1],
            [1, 1, 0]
        ], [
            [1, 0, 1],
            [1, 0, 0]
        ])
