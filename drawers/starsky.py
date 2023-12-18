from utils import echo
from constants import STAR_PROBABILITY
import random

STAR_STRING = ['·', '•', '*', '♦', '+', '•', '·']
STAR_TIMING = [2, 1, 1, 3, 1, 1, 2]
STAR_STRING_LEN = len(STAR_STRING)
STAR_WAITING = [6, 9, 12, 15]
stars_in_sky = []


def define_starsky(width: int, height: int):
    global stars_in_sky
    stars_in_sky = []
    range_star_Strings = range(STAR_STRING_LEN)
    for x in range(width):
        for y in range(height):
            condition = random.random() < STAR_PROBABILITY
            if (condition):
                str_index = random.choice(range_star_Strings)
                waiting = random.choice(STAR_WAITING)
                stars_in_sky.append([x, y, str_index, waiting, 0])


def draw_starsky(terminal):
    global stars_in_sky
    if (len(stars_in_sky) == 0):
        define_starsky(terminal.width, terminal.height)
    star_index = 0
    for star in stars_in_sky:
        x, y, str_index, waiting, counter = star
        if str_index == 0:
            timing = STAR_TIMING[str_index] + waiting
        else:
            timing = STAR_TIMING[str_index]
        if (counter == 0):
            str_star = STAR_STRING[str_index]
            echo(terminal.move_xy(x, y))
            echo(str_star)
        if (counter == timing):
            counter = 0
            str_index += 1
            if (str_index >= STAR_STRING_LEN):
                str_index = 0
        else:
            counter += 1
        stars_in_sky[star_index][2] = str_index
        stars_in_sky[star_index][4] = counter
        star_index += 1
