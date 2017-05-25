
"""

Imagine a robot sitting in the upper left corner of an X by Y grid. 
The robot can only move right or down. How many possible solutions exist to move from (0,0) to (X,Y)?

Follow up: Imagine, some positions are blocked and the robot cannot cross them.


"""


class GridPaths:

    def __init__(self):

        self.count = 0

    def traverse_grid(self, x, y):

        if x == 0 and y == 0:

            self.count += 1

        else:

            if x > 0 and y == 0:

                return self.traverse_grid(x-1, y)

            elif x == 0 and y > 0:

                return self.traverse_grid(y-1, x)

            else:

                return self.traverse_grid(y-1, x), self.traverse_grid(y, x-1)
