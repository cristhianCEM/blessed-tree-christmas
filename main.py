import blessed
import random
import math
import time

from utils import echo, get_text_formatted
from drawers.starsky import draw_starsky
from drawers.moon import draw_full_moon
from drawers.tree import draw_base_star, draw_base_tree, draw_fairy_lights

MESSAGE = 'Feliz Navidad!'
MESSAGE_FONT = 'contessa'
MESSAGE_HEIGHT = 3
MESSAGE_QUIT = 'Press Q to quit.'
LEN_MESSAGE_QUIT = len(MESSAGE_QUIT)


def draw_message_quit(terminal):
    echo(terminal.move_yx(terminal.height, terminal.width - LEN_MESSAGE_QUIT))
    echo(terminal.bright_black(MESSAGE_QUIT))


def draw_message(terminal):
    echo(terminal.move_yx(terminal.height - MESSAGE_HEIGHT, 0))
    echo(terminal.red(get_text_formatted(MESSAGE, font=MESSAGE_FONT)))


def setup(terminal):
    echo(terminal.on_black(terminal.clear()))
    echo(terminal.move_xy(0, 0))
    draw_starsky(terminal, True)
    draw_full_moon(terminal, True)
    draw_base_star(terminal, True)
    draw_base_tree(terminal, True)
    draw_message(terminal)
    draw_message_quit(terminal)


def loop(terminal):
    draw_starsky(terminal, False)
    draw_full_moon(terminal, False)
    draw_fairy_lights(terminal)


def main():
    terminal = blessed.Terminal()
    with terminal.hidden_cursor(), terminal.cbreak(), terminal.location():
        current_width, current_height = terminal.width, terminal.height
        setup(terminal)
        input = None
        while input not in (u'q', u'Q'):
            width, height = terminal.width, terminal.height
            if current_width != width or current_height != height:
                current_width, current_height = width, height
                setup(terminal)
            else:
                loop(terminal)
            input = terminal.inkey(timeout=0.1)


if __name__ == '__main__':
    main()
