import math
from utils.colors import random_color
import random

MOON = [
    "#########___---___",
    "######.-'         '-.",
    "####./   ()      .-. \.",
    "###/   o    .   (:::)  \ ",
    "##/ .            '-'    \ ",
    "#| ()   ::  O         .  |",
    "|                         |",
    "|    o           ()       |",
    "|       .::.          O   |",
    "#| .   ::::::            |",
    "##\     ::::     ::  .  /",
    "###\                   /",
    "####`\  o    ()      /'",
    "######`--_       _--'",
    "##########''---''"
]

MOON_DEPTH = 1
MOON_COLOR = (255, 255, 255, 1)
moon_x = 0
moon_y = 0


def draw_full_moon(scene, reset: bool = False):
    global moon_x, moon_y
    if (reset):
        moon_x = math.floor(scene.width / 10)
        moon_y = math.floor(scene.height / 10)
    for i in range(len(MOON)):
        string = MOON[i]
        cantidad = string.count('#')
        string = string.replace('#', '')
        m_x = moon_x + cantidad
        m_y = moon_y + i
        scene.set_message(m_x, m_y, MOON_DEPTH, string, MOON_COLOR)


HO = "HO!"
SANTA = [
    "  __,--,                               ',/",
    " | \_,,\G        .,}    .,/    .,;  ,--')`",
    ' \ *__\(~)\,---,__/>_ ,__/>_ ,__/>-`//">>',
    '_/=#===#=(_,   /;"/> `/;">> `/;">>',
]
SANTA_TIMMING = 3
SANTA_WIDTH = len(SANTA[0])
SANTA_DEPTH = 2
SANTA_COLOR = (248, 213, 0, 1)
santa_x = 0
santa_y = 0
santa_count = 0


def draw_santa(scene, reset: bool = False):
    global santa_x, santa_y, santa_count
    if (reset):
        santa_x = math.floor(scene.width * 0.55)
        santa_y = math.floor(scene.height * 0.15)
    else:
        if (santa_count == SANTA_TIMMING):
            santa_count = 0
            maximo = scene.width + 5
            if (santa_x > maximo):
                santa_x = -SANTA_WIDTH
            else:
                santa_x += 1
        else:
            santa_count += 1
    for y in range(len(SANTA)):
        string = SANTA[y]
        for x in range(len(string)):
            caracter = string[x]
            tmp_x = santa_x + x
            tmp_y = santa_y + y
            if (tmp_x < 0):
                continue
            if (caracter != ' '):
                scene.set_point(tmp_x, tmp_y, SANTA_DEPTH,
                                string[x], SANTA_COLOR)
            else:
                scene.del_point(tmp_x, tmp_y, SANTA_DEPTH)
        if (santa_x > 0):
            scene.del_point(santa_x - 1, santa_y + y, SANTA_DEPTH)
