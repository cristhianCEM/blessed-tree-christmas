import numpy as np
from utils.console import echo, rgb_color

COLOR_WHITE = (255, 255, 255, 0)


class ConsoleMap3d(object):
    terminal = None
    width, height, depth = None, None, None
    space = None
    last_space = None

    def __init__(self, terminal, depth: int = 0):
        self.terminal = terminal
        self.depth = depth
        echo(terminal.on_black(terminal.clear()))
        echo(terminal.move_xy(0, 0))
        self.check_resize()

    def resize_to(self, width: int, height: int, depth: int = 0):
        self.width = width
        self.height = height
        self.depth = depth
        shape = (width, height, depth)
        self.space = np.zeros(shape, dtype=object)
        self.last_space = self.space.copy()

    def check_resize(self):
        new_width, new_height = self.terminal.width, self.terminal.height
        if self.width != new_width or self.height != new_height:
            self.resize_to(new_width, new_height, self.depth)
            print('Resized to: ', new_width, new_height)

    def set_point(self, x: int, y: int, z: int, caracter: str, color: tuple):
        self.space[x][y][z] = (caracter, color)

    def del_point(self, x: int, y: int, z: int):
        self.space[x][y][z] = 0

    def draw(self):
        # for y in range(self.height):
        #     text = ''
        #     echo(self.terminal.move_xy(0, y))
        #     for x in range(self.width):
        #         position = self.space[x][y]
        #         caracter = ' '
        #         color = None
        #         for z in range(self.depth):
        #             item = position[z]
        #             if item != 0:
        #                 caracter, color = item
        #         if color is None:
        #             text += caracter
        #         else:
        #             text += rgb_color(self.terminal, color, caracter)
        #     echo(self.terminal.on_black(text))

        for y in range(self.height):
            for x in range(self.width):
                last_position = self.last_space[x][y]
                position = self.space[x][y]
                if last_position.any() == position.any():
                    continue
                caracter = ' '
                color = COLOR_WHITE
                for z in range(self.depth):
                    item = position[z]
                    if item != 0:
                        caracter, color = item
                echo(self.terminal.move_xy(x, y))
                echo(rgb_color(self.terminal, color, caracter))
        self.last_space = self.space.copy()
