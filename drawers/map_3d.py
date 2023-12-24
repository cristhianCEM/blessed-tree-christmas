import numpy as np
from utils.colors import hsl_mix_rgba_colors
from utils.console import echo, rgb_color


class ConsoleMap3d(object):
    terminal = None
    width = None
    height = None
    depth = None
    space = None

    def __init__(self, terminal, depth: int = 0):
        self.terminal = terminal
        self.depth = depth
        self.resize()

    def resize_to(self, width: int, height: int, depth: int = 0):
        self.width = width
        self.height = height
        self.depth = depth
        self.space = np.zeros((self.width, self.height, self.depth), dtype=int)

    def check_resize(self):
        new_width, new_height = self.terminal.width, self.terminal.height
        if self.width != new_width or self.height != new_height:
            self.resize_to(new_width, new_height, self.depth)

    def set_point(self, x: int, y: int, z: int, caracter: str, color: tuple = (0, 0, 0, 0)):
        self.space[x][y][z] = [caracter, color]

    def del_point(self, x: int, y: int, z: int):
        self.space[x][y][z] = 0

    def draw(self):
        for y in range(self.height):
            text = ''
            echo(self.terminal.move_xy(0, y))
            for x in range(self.width):
                position = self.space[x][y]
                caracter = ' '
                color = None
                for z in range(self.depth):
                    item = position[z]
                    if item != 0:
                        caracter, color = item
                if color is None:
                    text += caracter
                else:
                    text += rgb_color(self.terminal, color, caracter)
            echo(self.terminal.on_black(text))
