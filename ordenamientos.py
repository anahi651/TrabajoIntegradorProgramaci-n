import timeit
import random

# ------------------- ALGORITMOS DE ORDENAMIENTO -------------------

def ordenamiento_burbuja(lista):
    """
    Ordena una lista usando el algoritmo de burbuja.
    Compara elementos adyacentes y los intercambia si están desordenados.
    Devuelve una nueva lista ordenada de menor a mayor.
    """
    lista = lista.copy()  # Copia para no modificar la original
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def ordenamiento_seleccion(lista):
    """
    Ordena una lista usando el algoritmo de selección.
    Busca el elemento más pequeño y lo coloca al principio.
    Devuelve una nueva lista ordenada de menor a mayor.
    """
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def ordenamiento_python(lista):
    """
    Ordena una lista usando la función sorted() de Python.
    Esta función es muy eficiente y no modifica la lista original.
    """
    return sorted(lista)

# ------------------- PRUEBA DE RENDIMIENTO -------------------

def prueba_ordenamiento(funcion, lista):
    """
    Mide el tiempo de ejecución de una función de ordenamiento.
    Ejecuta la función una vez sobre la lista y devuelve el tiempo en segundos.
    """
    tiempo = timeit.timeit(lambda: funcion(lista), number=1)
    return tiempo

# ------------------- CÓDIGO DE PRUEBA -------------------

if __name__ == "__main__":
    # Listas de diferentes tamaños para comparar rendimiento
    tamanos = [100, 500, 1000]
    print("Comparación de tiempos de ordenamiento (en segundos):")
    print("{:<10} {:<15} {:<15} {:<15}".format("Tamaño", "Burbuja", "Selección", "Sorted()"))

    for tamano in tamanos:
        # Genera una lista aleatoria sin elementos repetidos
        lista = random.sample(range(tamano * 10), tamano)

        # Calcula el tiempo de cada algoritmo
        t_burbuja = prueba_ordenamiento(ordenamiento_burbuja, lista)
        t_seleccion = prueba_ordenamiento(ordenamiento_seleccion, lista)
        t_sorted = prueba_ordenamiento(ordenamiento_python, lista)

        # Muestra los resultados
        print("{:<10} {:<15.5f} {:<15.5f} {:<15.5f}".format(
            tamano, t_burbuja, t_seleccion, t_sorted))
