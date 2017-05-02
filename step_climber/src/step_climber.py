"""

A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time. 
Implement a method to count how many possible ways the child can run up the stairs.

"""
from copy import copy, deepcopy


class StairTooShortException(Exception):

    def __init__(self):

        print ("The stair must not be flat!")


class Stair:

    def __init__(self, stair_length: int):

        if stair_length == 0:

            raise StairTooShortException

        self.length = stair_length


class Position:

    def __init__(self, height: int, remaining: int):

        self.height = height

        self.remaining = remaining

    def __repr__(self):

        return "{} steps left".format(self.remaining)


class Climber:

    def __init__(self, steps_allowed: tuple):

        self.steps_allowed = steps_allowed

        self.path_count = 0

        self.climb = None

        self.current_iteration = None

        self.next_iteration = []

    def __repr__(self):

        return "Climbs {} steps ahead".format(self.steps_allowed)

    def start_climbing(self, stair: Stair):

        self.climb = stair

        self.next_iteration.extend(self.create_next(Position(height=0, remaining=stair.length)))

        while len(self.next_iteration) > 0:

            self.current_iteration = deepcopy(self.next_iteration)

            self.next_iteration = []

            for node in self.current_iteration:

                if node.remaining == 0:

                    self.path_count += 1

                else:

                    self.next_iteration.extend(self.create_next(node))

    def create_next(self, node: Position):

        possible_steps = []

        for option in self.steps_allowed:

            if node.remaining >= option:

                possible_steps.append(Position(height=node.height+option,
                                               remaining=self.climb.length - (node.height+option)))

        return possible_steps


if __name__ == '__main__':

    ladder = Stair(12)

    hiker = Climber(steps_allowed = (2, 3, 4))

    hiker.start_climbing(stair=ladder)

    print (hiker.path_count)
