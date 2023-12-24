import time


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
