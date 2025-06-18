import random

def generar_lista_ordenada(tamano):
    """
    Genera una lista de números enteros únicos ordenados de menor a mayor.

    Parámetros:
    - tamano: cantidad de elementos que tendrá la lista

    Retorna:
    - Una lista ordenada con 'tamano' números aleatorios no repetidos.
    """
    # Genera una muestra aleatoria sin repetidos y la ordena
    return sorted(random.sample(range(tamano * 10), tamano))
