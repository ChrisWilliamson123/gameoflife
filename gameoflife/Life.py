import sys
class Life(object):

    def __init__(self, state):
        self.state = state

    def neighbours(self, coords):
        """
        Returns a set containing the coordinates of the specified cells neighbours
        """
        neighbours_set = set()
        x = coords[0]
        y = coords[1]
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (i, j) != (x, y):
                    neighbours_set.add((i, j))
        return neighbours_set

    def evolve(self):
        next_state = set()
        for cell in self.state:
            neighbours = self.neighbours(cell)
            # Get the intersection of the current state and the neighbours
            # This gives us the coords of the cells alive neighbours
            alive_neighbours = set(neighbours & self.state)
            if len(alive_neighbours) == 2 or len(alive_neighbours) == 3:
                next_state.add(cell)

            for n_cell in neighbours:
                n_cell_alive_neighbours = set(self.neighbours(n_cell) & self.state)
                if len(n_cell_alive_neighbours) == 3:
                    next_state.add(n_cell)
        self.state = next_state
