from utils.console import get_text_formatted
from utils.colors import random_color

SCENE_DEPTH = 5
SCENE_Z = SCENE_DEPTH - 1
MESSAGE = 'Feliz Navidad!'
MESSAGE_FONT = 'contessa'
MESSAGE_COLOR = (255, 0, 0, 1)

QUIT_MESSAGE = 'Press Q to quit.'
QUIT_MESSAGE_COLOR = (167, 117, 255, 1)

DECORACTION = ".:*~*:._"
DECORACTION_COLOR = (255, 255, 255, 1)


def draw_message_quit(scene):
    msg_x = scene.width - len(QUIT_MESSAGE)
    msg_y = scene.height - 1
    scene.set_message(msg_x, msg_y, SCENE_Z, QUIT_MESSAGE, QUIT_MESSAGE_COLOR)


def draw_message(scene):
    text = get_text_formatted(MESSAGE, font=MESSAGE_FONT)
    split_text = text.split('\n')
    msg_y = scene.height - len(split_text)
    for i, line in enumerate(split_text):
        scene.set_message(0, msg_y + i, SCENE_Z, line, MESSAGE_COLOR)


def draw_decorations(scene):
    pos_y = scene.height - 1
    for i in range(scene.width):
        caracter = DECORACTION[i % len(DECORACTION)]
        scene.set_point(i, pos_y, SCENE_Z, caracter, DECORACTION_COLOR)


def draw_ui(scene):
    draw_message(scene)
    draw_message_quit(scene)
