from busquedas import (
    busqueda_lineal,
    busqueda_binaria_iterativa,
    busqueda_binaria_recursiva
)

from ordenamientos import (
    ordenamiento_burbuja,
    ordenamiento_seleccion,
    ordenamiento_python,
    prueba_ordenamiento
)

from generador import generar_lista_ordenada
from pruebas import prueba_busqueda

import random

# ------------------- PRUEBAS DE BÚSQUEDA -------------------

# Tamaños de listas a usar para las pruebas de búsqueda
tamanos_busqueda = [10, 100, 1000, 10000, 100000]

print("\nTiempos de ejecución (en milisegundos) para 1000 ejecuciones de búsqueda:")
print("{:<10} {:<15} {:<15} {:<15}".format("Tamaño", "Lineal", "Binaria It.", "Binaria Rec."))

for tamano in tamanos_busqueda:
    # Se genera una lista ordenada de tamaño 'tamano'
    lista = generar_lista_ordenada(tamano)
    objetivo = random.choice(lista)  # Se elige un valor que sí está en la lista

    # Se mide el tiempo que tarda cada búsqueda en ejecutarse 1000 veces
    tiempo_lineal = prueba_busqueda(busqueda_lineal, lista, objetivo)
    tiempo_iter = prueba_busqueda(busqueda_binaria_iterativa, lista, objetivo)
    tiempo_rec = prueba_busqueda(busqueda_binaria_recursiva, lista, objetivo)

    # Se imprimen los resultados en milisegundos
    print("{:<10} {:<15.5f} {:<15.5f} {:<15.5f}".format(
        tamano, tiempo_lineal * 1000, tiempo_iter * 1000, tiempo_rec * 1000))

# Prueba adicional con un valor que NO está en la lista
print("\nPrueba con objetivo que NO está en la lista:")
objetivo = -1  # Valor que no existe en la lista
lista = generar_lista_ordenada(10000)

print("Lineal:", prueba_busqueda(busqueda_lineal, lista, objetivo) * 1000, "ms")
print("Binaria Iterativa:", prueba_busqueda(busqueda_binaria_iterativa, lista, objetivo) * 1000, "ms")
print("Binaria Recursiva:", prueba_busqueda(busqueda_binaria_recursiva, lista, objetivo) * 1000, "ms")

# Prueba con una lista pequeña como caso base
print("\nResultado con lista pequeña:")
lista_pequena = [1, 2, 3]
objetivo = 2

print("Resultado búsqueda lineal:", busqueda_lineal(lista_pequena, objetivo))
print("Resultado binaria iterativa:", busqueda_binaria_iterativa(lista_pequena, objetivo))
print("Resultado binaria recursiva:", busqueda_binaria_recursiva(lista_pequena, objetivo))

# ------------------- PRUEBAS DE ORDENAMIENTO -------------------

print("\nComparación de tiempos de ordenamiento (en segundos):")
print("{:<10} {:<15} {:<15} {:<15}".format("Tamaño", "Burbuja", "Selección", "Sorted()"))

# Tamaños de listas a probar con los algoritmos de ordenamiento
for tamano in [100, 500, 1000]:
    # Genera una lista aleatoria de números únicos
    lista = random.sample(range(tamano * 10), tamano)

    # Mide el tiempo de ejecución de cada algoritmo
    t_burbuja = prueba_ordenamiento(ordenamiento_burbuja, lista)
    t_seleccion = prueba_ordenamiento(ordenamiento_seleccion, lista)
    t_sorted = prueba_ordenamiento(ordenamiento_python, lista)

    # Imprime los resultados de cada ordenamiento
    print("{:<10} {:<15.5f} {:<15.5f} {:<15.5f}".format(
        tamano, t_burbuja, t_seleccion, t_sorted))
