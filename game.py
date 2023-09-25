import pyxel

from utils import (
    BACKGROUND_COLOR,
    DEFAULT_MAZE,
    END_COORDINATES,
    KEY_COMBINATIONS,
    WALL_SYMBOL,
    Coordinates,
)


class Maze:
    players_coordinates = Coordinates(0, 0)

    def __init__(self) -> None:
        self.maze = DEFAULT_MAZE
        self.set_cell(0, 0, 2)
        pyxel.init(len(self.maze), len(self.maze[0]), fps=15, title="Maze game")

        pyxel.run(self.update, self.draw)

    def update(self):
        for combination in KEY_COMBINATIONS:
            if pyxel.btn(combination[0]):
                new_coords = self.players_coordinates + combination[1]
                if new_coords == END_COORDINATES:
                    pyxel.quit()
                elif self.maze[new_coords[1]][new_coords[0]] != WALL_SYMBOL:
                    self.set_cell(
                        self.players_coordinates[0], self.players_coordinates[1], 0
                    )
                    self.set_cell(new_coords[0], new_coords[1], 2)
                    self.players_coordinates = new_coords

    def set_cell(self, x, y, value):
        self.maze[y][x] = value

    def draw(self):
        pyxel.cls(BACKGROUND_COLOR)

        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                pyxel.pset(
                    x, y, BACKGROUND_COLOR if not cell else (1 if cell == 1 else 4)
                )


Maze()
