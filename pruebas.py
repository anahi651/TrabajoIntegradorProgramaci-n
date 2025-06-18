import timeit

def prueba_busqueda(funcion, lista, objetivo):
    """
    Mide el tiempo que tarda una función de búsqueda en ejecutarse 1000 veces.

    Parámetros:
    - funcion: función de búsqueda a probar (ej: busqueda_lineal)
    - lista: lista sobre la que se va a buscar
    - objetivo: valor a buscar dentro de la lista

    Retorna:
    - Tiempo total (en segundos) que tarda en ejecutarse la función 1000 veces.
    """
    tiempo = timeit.timeit(lambda: funcion(lista, objetivo), number=1000)
    return tiempo
