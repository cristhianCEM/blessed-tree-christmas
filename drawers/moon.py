import math

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
