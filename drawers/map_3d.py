import numpy as np
from utils.console import echo, rgb_color
from utils.image import count_drawn_pixels
from utils.colors import hsl_mix_rgba_colors

COLOR_WHITE = (255, 255, 255, 0)


class ConsoleMap3d(object):
    terminal = None
    width, height, depth = None, None, None
    space = None
    last_space = None
    setup: callable = None

    def __init__(self, terminal, setup: callable = None, depth: int = 0):
        self.terminal = terminal
        self.depth = depth
        self.setup = setup
        self.check_resize()

    def terminal_clear(self):
        echo(self.terminal.on_black(self.terminal.clear()))

    def resize_to(self, width: int, height: int, depth: int = 0):
        self.width = width
        self.height = height
        self.depth = depth
        shape = (width, height, depth)
        self.space = np.zeros(shape, dtype=object)
        self.before_space = self.space.copy()
        self.terminal_clear()
        self.setup(self)

    def check_resize(self):
        new_width, new_height = self.terminal.width, self.terminal.height
        if self.width != new_width or self.height != new_height:
            self.resize_to(new_width, new_height, self.depth)

    def set_point(self, x: int, y: int, z: int, caracter: str, color: tuple):
        try:
            self.space[x][y][z] = (caracter, color)
        except IndexError:
            pass

    def set_message(self, x: int, y: int, z: int, message: str, color: tuple):
        for i, caracter in enumerate(message):
            self.set_point(x + i, y, z, caracter, color)

    def del_point(self, x: int, y: int, z: int):
        try:
            self.space[x][y][z] = 0
        except IndexError:
            pass

    def merge_colors(self, colors: list):
        color = colors[0]
        color_alpha = color[3]
        if color_alpha == 1:
            return color
        for tmp_color in colors[1:]:
            color = hsl_mix_rgba_colors(color, tmp_color)
            color_alpha = tmp_color[3]
            if color_alpha == 1:
                break
        return color

    def merge_caracters(self, caracters_to_merge: list):
        max_count = 0
        caracter_final = caracters_to_merge[0]
        for caracter in caracters_to_merge:
            count = count_drawn_pixels(caracter)
            if count > max_count:
                max_count = count
                caracter_final = caracter
        return caracter_final

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                # revisar si cambio algo
                last_position = self.before_space[x][y]
                position = self.space[x][y]
                if last_position.any() == position.any():
                    continue
                # set default values
                caracter = ''
                color = COLOR_WHITE
                # obtener array colores y caracteres a mezclar
                colors_to_merge = []
                caracters_to_merge = []
                for z in range(self.depth - 1, -1, -1):
                    item = position[z]
                    if item != 0:
                        tmp_caracter, tmp_color = item
                        colors_to_merge.append(tmp_color)
                        if tmp_caracter != '':
                            caracters_to_merge.append(tmp_caracter)
                # mezclar colores y caracteres
                if len(caracters_to_merge) == 0:
                    continue
                color = self.merge_colors(colors_to_merge)
                caracter = self.merge_caracters(caracters_to_merge)
                # iniciar dibujo
                echo(self.terminal.move_xy(x, y))
                echo(rgb_color(self.terminal, color, caracter))
        self.before_space = self.space.copy()
