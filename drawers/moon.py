import math
from utils.colors import random_color

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
SANTA_DEPTH = 3
SANTA_COLOR = (255, 101, 80, 1)
santa_x = 0
santa_y = 0
santa_timming = 10


def draw_santa(scene, reset: bool = False):
    global santa_x, santa_y
    if (reset):
        santa_x = math.floor(scene.width * 0.30)
        santa_y = math.floor(scene.height * 0.12)
    for i in range(len(SANTA)):
        string = SANTA[i]
        for j in range(len(string)):
            if string[j] != ' ':
                scene.set_point(santa_x + j, santa_y + i,
                                SANTA_DEPTH, string[j], SANTA_COLOR)
