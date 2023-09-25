import random

import pyxel


def create_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def carve_path(x, y):
        # Mark the current cell as a path (0)
        maze[y][x] = 0

        # Create a list of possible directions to move (up, down, left, right)
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < width and 0 <= new_y < height:
                if maze[new_y][new_x] == 1:
                    maze[y + dy // 2][x + dx // 2] = 0
                    carve_path(new_x, new_y)

    # Start carving the path from a random starting point
    start_x = random.randrange(0, width, 2)
    start_y = random.randrange(0, height, 2)
    carve_path(start_x, start_y)

    return maze


DEFAULT_MAZE = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 0],
]


BACKGROUND_COLOR = 0
WALL_COLOR = 7
WALL_SYMBOL = 1


class Coordinates:
    def __init__(self, x, y) -> None:
        self.coords = (x, y)

    def __add__(self, val2):
        return Coordinates(
            self.coords[0] + val2.coords[0], self.coords[1] + val2.coords[1]
        )

    def __getitem__(self, slice):
        return self.coords[slice]

    def __eq__(self, val2) -> bool:
        return self.coords == val2.coords

    def __str__(self) -> str:
        return str(self.coords)


START_COORDINATES = Coordinates(0, 0)
END_COORDINATES = Coordinates(len(DEFAULT_MAZE[1]) - 1, len(DEFAULT_MAZE) - 1)

UP = Coordinates(0, -1)
DOWN = Coordinates(0, 1)
LEFT = Coordinates(-1, 0)
RIGHT = Coordinates(1, 0)


KEY_COMBINATIONS = [
    (pyxel.KEY_UP, UP),
    (pyxel.KEY_DOWN, DOWN),
    (pyxel.KEY_LEFT, LEFT),
    (pyxel.KEY_RIGHT, RIGHT),
]
