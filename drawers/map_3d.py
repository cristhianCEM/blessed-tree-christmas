import numpy as np
from utils.colors import hsl_mix_rgba_colors


class ConsoleMap3d(object):
    terminal = None
    width = None
    height = None
    depth = None
    map = None

    def __init__(self, terminal, depth: int = 0):
        self.terminal = terminal
        self.depth = depth
        self.resize()

    def resize_to(self, width: int, height: int, depth: int = 0):
        self.width = width
        self.height = height
        self.depth = depth
        self.map = np.zeros((self.width, self.height, self.depth), dtype=int)

    def resize(self):
        self.resize(self.terminal.width, self.terminal.height, self.depth)
