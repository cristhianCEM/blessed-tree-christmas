from utils import echo
import math

BIG_MOON = [
    "#########___---___",
    "######.-'         '-.",
    "####./   ()      .-. \.",
    "###/   o    .   (   )  \ ",
    "##/ .            '-'    \ ",
    "#| ()    .  O         .  |",
    "|                         |",
    "|    o           ()       |",
    "|       .--.          O   |",
    "#| .   |    |            |",
    "##\    `.__.'    o   .  /",
    "###\                   /",
    "####`\  o    ()      /'",
    "######`--_       _--'",
    "######### ''---''"
]

TRANSLATE_MOON = [
    [
    "   _..._",
    " .:::::::.",
    ":::::::::::",
    ":::::::::::",
    "`:::::::::'",
    "  `':::''",
    ], [
    "   _..._",
    " .::::. `.",
    ":::::::.  :",
    "::::::::  :",
    "`::::::' .'",
    "  `'::'-'",
    ], [
    "   _..._",
    " .::::  `.",
    "::::::    :",
    "::::::    :",
    "`:::::   .'",
    "  `'::.-'",
    ], [
    "   _..._",
    " .::'   `.",
    ":::       :",
    ":::       :",
    "`::.     .'",
    "  `':..-'",
    ], [
    "   _..._",
    " .'     `.",
    ":         :",
    ":         :",
    "`.       .'",
    "  `-...-'",
    ], [
    "   _..._",
    " .'   `::.",
    ":       :::",
    ":       :::",
    "`.     .::'",
    "  `-..:''",
    ], [
    "   _..._",
    " .'  ::::.",
    ":    ::::::",
    ":    ::::::",
    "`.   :::::'",
    "  `-.::''",
    ], [
    "   _..._",
    " .' .::::.",
    ":  ::::::::",
    ":  ::::::::",
    "`. '::::::'",
    "  `-.::''",
    ], [
    "   _..._",
    " .:::::::.",
    ":::::::::::",
    ":::::::::::",
    "`:::::::::'",
    "  `':::''",
    ]
]
TRANSLATE_MOON_LEN = len(TRANSLATE_MOON)
TRANSLATE_MOON_TIMING = [10, 10, 10, 10, 10, 10, 10, 10, 10]
moon_index = 0
moon_counter = 0
moon_x = 0
moon_y = 0

def draw_big_moon(terminal, x, y):
    for i in range(len(BIG_MOON)):
        string = BIG_MOON[i]
        cantidad = string.count('#')
        string = string.replace('#', '')
        echo(terminal.move_xy(x + cantidad, y + i))
        echo(terminal.on_black(terminal.bright_white(string)))

def draw_translate_moon(terminal, reset: bool = False):
    global moon_index, moon_counter, moon_x, moon_y
    if (reset):
        moon_index = 0
        moon_counter = 0
        moon_x = math.floor(terminal.width / 10)
        moon_y = math.floor(terminal.height / 10)
    timming = TRANSLATE_MOON_TIMING[moon_index]
    if (moon_counter == 0):
        moon_index += 1
        if (moon_index >= TRANSLATE_MOON_LEN):
            moon_index = 0
    if (moon_counter == timming):
        moon_counter = 0
    else:
        moon_counter += 1
    moon = TRANSLATE_MOON[moon_index]
    for i in range(len(moon)):
        string = moon[i]
        # cantidad = string.count(':')
        # string = string.replace(':', '')
        echo(terminal.move_xy(moon_x, moon_y + i))
        echo(terminal.on_black(terminal.bright_white(string)))