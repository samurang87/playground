
"""

Imagine a robot sitting in the upper left corner of an X by Y grid. 
The robot can only move right or down. How many possible solutions exist to move from (0,0) to (X,Y)?

Follow up: Imagine, some positions are blocked and the robot cannot cross them.


"""


class Grid:

    """
    blocks: list of x,y tuples
    """

    def __init__(self, blocks=None):

        self.count = 0

        self.blocks = blocks

    def traverse_grid(self, x, y):

        if self.blocks and (x, y) in self.blocks:

            return

        if x == 0 and y == 0:

            self.count += 1

        else:

            if x > 0 and y == 0:

                return self.traverse_grid(x-1, y)

            elif x == 0 and y > 0:

                return self.traverse_grid(y-1, x)

            else:

                return self.traverse_grid(y-1, x), self.traverse_grid(y, x-1)
