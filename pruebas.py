import timeit

def prueba_busqueda(funcion, lista, objetivo):
    # Usamos timeit para medir el tiempo
    tiempo = timeit.timeit(lambda: funcion(lista, objetivo), number=1000)
    return tiempo