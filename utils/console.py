import sys
import pyfiglet


def echo_python2(text):
    """Función 'echo' para Python 2: Imprime sin añadir salto de línea y vacía el buffer."""
    sys.stdout.write(u'{0}'.format(text))
    sys.stdout.flush()


def echo_python3(text):
    """
    Función 'echo' para Python 3: Imprime sin añadir salto de línea y vacía el buffer.
    """
    print(text, end='', flush=True)


# Determina si estamos usando Python 2 o 3 y asigna la función 'echo' correspondiente
if sys.version_info[0] < 3:
    echo = echo_python2
else:
    echo = echo_python3


def rgb_color(terminal, color: list, text: str):
    """
    Devuelve el texto formateado con el color indicado.
    """
    r, g, b, _ = color
    return f"\x1b[38;2;{r};{g};{b}m{text}{terminal.normal}"


def get_text_formatted(text: str, font: str):
    """
    Devuelve el texto formateado con la fuente indicada.
    """
    text = pyfiglet.figlet_format(text, font=font)
    text_split = text.split('\n')
    result = '\n'.join(line for line in text_split if line.strip())
    return result
