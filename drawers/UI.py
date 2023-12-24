from utils.console import echo, get_text_formatted, rgb_color

MESSAGE = 'Feliz Navidad!'
MESSAGE_FONT = 'contessa'
MESSAGE_HEIGHT = 3
MESSAGE_QUIT = 'Press Q to quit.'
LEN_MESSAGE_QUIT = len(MESSAGE_QUIT)
occupied_positions = []

def draw_message_quit(terminal):
    echo(terminal.move_yx(terminal.height, terminal.width - LEN_MESSAGE_QUIT))
    # echo(terminal.bright_black(MESSAGE_QUIT))
    echo(rgb_color(terminal, 80, 25, 80, MESSAGE_QUIT))


def draw_message(terminal):
    echo(terminal.move_yx(terminal.height - MESSAGE_HEIGHT, 0))
    echo(terminal.red(get_text_formatted(MESSAGE, font=MESSAGE_FONT)))
