# main.py

from busquedas import busqueda_binaria_iterativa, busqueda_binaria_recursiva
from generador import generar_lista_ordenada
from pruebas import prueba_busqueda
import random

tamanos = [10, 100, 1000, 10000, 100000, 1000000]

print("Tiempos de ejecución (en milisegundos) para 1000 ejecuciones:")
print("{:<10} {:<20} {:<20}".format("Tamaño", "Iterativa", "Recursiva"))

for tamano in tamanos:
    lista = generar_lista_ordenada(tamano)
    objetivo = random.choice(lista)

    tiempo_iter = prueba_busqueda(busqueda_binaria_iterativa, lista, objetivo)
    tiempo_rec = prueba_busqueda(busqueda_binaria_recursiva, lista, objetivo)

    print("{:<10} {:<20.5f} {:<20.5f}".format(
        tamano, tiempo_iter * 1000, tiempo_rec * 1000))

# Prueba adicional con objetivo inexistente
objetivo = -1
tiempo_iter = prueba_busqueda(busqueda_binaria_iterativa, lista, objetivo)
tiempo_rec = prueba_busqueda(busqueda_binaria_recursiva, lista, objetivo)

# Prueba con lista pequeña
lista_pequena = [1, 2, 3]
objetivo = 2
print("\nResultado con lista pequeña:", busqueda_binaria_iterativa(lista_pequena, objetivo))
