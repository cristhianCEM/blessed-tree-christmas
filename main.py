import blessed
from utils import echo
from drawers.starsky import draw_starsky
from drawers.moon import draw_full_moon
from drawers.tree import draw_base_star, draw_base_tree, draw_fairy_lights
from drawers.UI import draw_message, draw_message_quit


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
