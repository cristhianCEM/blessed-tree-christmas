from utils import echo

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

def draw_big_moon(terminal, x, y):
    for i in range(len(BIG_MOON)):
        string = BIG_MOON[i]
        cantidad = string.count('#')
        string = string.replace('#', '')
        echo(terminal.move_xy(x + cantidad, y + i))
        echo(terminal.on_black(terminal.bright_white(string)))

def draw_translate_moon(terminal, x, y):
    global moon_index, moon_counter
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
        echo(terminal.move_xy(x, y + i))
        echo(terminal.on_black(terminal.bright_white(string)))