import sys

def echo_python2(text):
    """Función 'echo' para Python 2: Imprime sin añadir salto de línea y vacía el buffer."""
    sys.stdout.write(u'{0}'.format(text))
    sys.stdout.flush()

def echo_python3(text):
    """Función 'echo' para Python 3: Imprime sin añadir salto de línea y vacía el buffer."""
    print(text, end='', flush=True)

# Determina si estamos usando Python 2 o 3 y asigna la función 'echo' correspondiente
if sys.version_info[0] < 3:
    echo = echo_python2
else:
    echo = echo_python3