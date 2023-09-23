import pyxel
from random import randint

LARGEUR = 30
HAUTEUR = 20
# COULEUR_FOND = randint(0, 15)
BACKGROUND_COLOR = 0
WALL_COLOR = 7


class Coordinates:
    def __init__(self, x, y) -> None:
        self.coords = (x, y)

    def __add__(self, val2):
        return Coordinates(
            self.coords[0] + val2.coords[0], self.coords[1] + val2.coords[1]
        )

    def __getitem__(self, slice):
        return self.coords[slice]

    def __eq__(self, __value) -> bool:
        return self.coords == __value.coords


UP = Coordinates(0, -1)
DOWN = Coordinates(0, 1)
LEFT = Coordinates(-1, 0)
RIGHT = Coordinates(1, 0)

maze = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 0],
]

START_COORDINATES = Coordinates(0, 0)
END_COORDINATES = Coordinates(len(maze[1]) - 1, len(maze) - 1)
WALL_SYMBOL = 1


def get_random_screen():
    return Coordinates(randint(0, LARGEUR), randint(0, HAUTEUR))


class Maze:
    players_coordinates = Coordinates(0, 0)

    def __init__(self) -> None:
        maze = self.get_initial_maze()
        pyxel.init(len(maze), len(maze[0]), fps=5, title="Maze game")

        pyxel.run(self.update, self.draw)

    def get_initial_maze(self):
        return [
            [0, 1, 1, 1],
            [0, 0, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 0],
        ]

    def update(self):
        for key in [
            (pyxel.KEY_UP, UP),
            (pyxel.KEY_DOWN, DOWN),
            (pyxel.KEY_LEFT, LEFT),
            (pyxel.KEY_RIGHT, RIGHT),
        ]:
            if pyxel.btn(key[0]):
                new_coords = self.players_coordinates + key[1]
                if new_coords == END_COORDINATES:
                    pyxel.quit()
                if new_coords[0] >= len(self.get_initial_maze()[0]) or new_coords[
                    1
                ] >= len(self.get_initial_maze()):
                    print("out of bounds", new_coords.coords)
                    continue
                if maze[new_coords[1]][new_coords[0]] != WALL_SYMBOL:
                    self.players_coordinates = new_coords

    def get_updated_maze(self):
        maze = self.get_initial_maze()
        maze[self.players_coordinates[1]][self.players_coordinates[0]] = 2

        return maze

    def draw(self):
        maze = self.get_updated_maze()
        pyxel.cls(BACKGROUND_COLOR)

        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                color = -1
                match cell:
                    case 0:
                        color = BACKGROUND_COLOR
                    case 1:
                        color = WALL_COLOR
                    case _:
                        color = 4
                pyxel.pset(x, y, color)


Maze()
