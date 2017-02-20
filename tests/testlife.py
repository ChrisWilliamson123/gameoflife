from gameoflife.Life import Life
import unittest

class testLife(unittest.TestCase):

    def normalise_coords(self, coords):
        """
        Takes a set of coordinates and if needed, shifts them to be all positive.
        Used to make it easier to compare sets.
        """
        if not len(coords):
            return set()

        rows = sorted([x[0] for x in coords])
        columns = sorted([x[1] for x in coords])
        row_shift = rows[0] * -1 if rows[0] < 0 else 0
        column_shift = columns[0] * -1 if columns[0] < 0 else 0
        new_coords = set()
        for cell in coords:
            new_coords.add((cell[0]+row_shift, cell[1]+column_shift))
        return new_coords

    def grid_to_coords(self, grid):
        """
        Converts a 2D list to a set of coordinates.
        """
        coords = set()
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
              if grid[i][j]:
                  coords.add((i, j))
        return self.normalise_coords(coords)

    def create_evolve_assert(self, initial_state, final_state, evolutions=1):
        testLife = Life(self.grid_to_coords(initial_state))
        for i in range(0, evolutions):
            testLife.evolve()
        self.assertEqual(self.grid_to_coords(final_state), self.normalise_coords(testLife.state))

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
            [0, 1, 0],
            [1, 0, 1],
            [1, 0, 1]
        ])

    def test_survival(self):
        """
        Tests that a cell stays alive if it has 2 or 3 neighbours.
        """
        self.create_evolve_assert([
            [1, 1],
            [1, 1]
        ], [
            [1, 1],
            [1, 1]
        ])

    def test_creation(self):
        """
        Tests that a cell comes to life if it has three neighbours.
        """
        self.create_evolve_assert([
            [0, 1],
            [1, 1]
        ], [
            [1, 1],
            [1, 1]
        ])

    def test_grid_expansion(self):
        """
        Tests that the grid expands if a new cell is to be added.
        """
        self.create_evolve_assert([
            [1, 1, 1]
        ], [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ])

    def test_two_iterations(self):
        """
        This is the example that we were given.
        After two iterations, result should be the same as the input.
        """
        self.create_evolve_assert([
            [1, 1, 1]
        ], [
            [1, 1, 1]
        ], 2)

    def test_three_iterations(self):
        """
        Tests three iterations
        """
        self.create_evolve_assert([
            [0, 1, 0, 1],
            [1, 1, 1, 1],
            [1, 0, 0, 1]
        ], [
            [1, 1, 0, 1, 0],
            [1, 0, 0, 1, 1],
            [1, 0, 0, 1, 0]
        ])
