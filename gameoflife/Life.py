import sys
class Life(object):

    def __init__(self, state):
        self.state = state

    def evolve(self):
        self.state = set()
