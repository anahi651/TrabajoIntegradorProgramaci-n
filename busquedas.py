# ------------------- ALGORITMOS DE BÚSQUEDA -------------------

def busqueda_lineal(lista, objetivo):
    """
    Realiza una búsqueda lineal sobre la lista.
    Recorre la lista desde el inicio hasta encontrar el valor objetivo.

    Parámetros:
    - lista: lista de elementos (no importa si está ordenada o no)
    - objetivo: valor a buscar

    Retorna:
    - Índice donde se encuentra el objetivo, o -1 si no está
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Se encontró el valor
    return -1  # No se encontró el valor


def busqueda_binaria_iterativa(lista, objetivo):
    """
    Realiza una búsqueda binaria iterativa en una lista ordenada.
    Divide la lista en mitades y compara el valor medio con el objetivo.

    Parámetros:
    - lista: lista ordenada de elementos
    - objetivo: valor a buscar

    Retorna:
    - Índice donde se encuentra el objetivo, o None si no está
    """
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio] == objetivo:
            return medio  # Se encontró el valor
        elif lista[medio] < objetivo:
            inicio = medio + 1  # Buscar en la mitad derecha
        else:
            fin = medio - 1  # Buscar en la mitad izquierda

    return None  # No se encontró el valor


def busqueda_binaria_recursiva(lista, objetivo, inicio=0, fin=None):
    """
    Realiza una búsqueda binaria recursiva en una lista ordenada.
    Llama a sí misma dividiendo la lista en mitades.

    Parámetros:
    - lista: lista ordenada de elementos
    - objetivo: valor a buscar
    - inicio: índice inicial del rango de búsqueda (por defecto 0)
    - fin: índice final del rango de búsqueda (por defecto último índice)

    Retorna:
    - Índice donde se encuentra el objetivo, o -1 si no está
    """
    if fin is None:
        fin = len(lista) - 1

    if inicio > fin:
        return -1  # Caso base: no se encontró el valor

    medio = (inicio + fin) // 2

    if lista[medio] == objetivo:
        return medio  # Se encontró el valor
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, fin)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, inicio, medio - 1)






    

