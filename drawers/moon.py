from utils import echo
import math

FULL_MOON = [
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
    "######### ''---''"
]

moon_x = 0
moon_y = 0

def draw_full_moon(terminal, reset: bool = False):
    global moon_x, moon_y
    if (reset):
        moon_x = math.floor(terminal.width / 10)
        moon_y = math.floor(terminal.height / 10)
    echo(terminal.on_black(terminal.bright_white('')))
    for i in range(len(FULL_MOON)):
        string = FULL_MOON[i]
        cantidad = string.count('#')
        string = string.replace('#', '')
        echo(terminal.move_xy(moon_x + cantidad, moon_y + i))
        echo(string)
