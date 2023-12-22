import sys
import time
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


def measure_time(func):
    """
    Decorador que mide el tiempo de ejecución de una función.
    """
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        print(f"- Iniciando {function_name} -")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed_time = end - start
        print(
            f"Tiempo transcurrido en {function_name}: {elapsed_time:.6f} segundos")
        return result
    return wrapper


def get_text_formatted(text: str, font: str):
    """
    Devuelve el texto formateado con la fuente indicada.
    """
    text = pyfiglet.figlet_format(text, font=font)
    text_split = text.split('\n')
    result = '\n'.join(line for line in text_split if line.strip())
    return result
