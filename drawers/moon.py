from utils import echo

MOON_MIDDLE = [
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

def draw_moon(terminal, x, y):
    for i in range(len(MOON_MIDDLE)):
        string = MOON_MIDDLE[i]
        cantidad = string.count('#')
        string = string.replace('#', '')
        echo(terminal.move_xy(x + cantidad, y + i))
        echo(terminal.on_black(terminal.bright_white(string)))
