# main.py

from busquedas import busqueda_binaria_iterativa, busqueda_binaria_recursiva, busqueda_lineal
from generador import generar_lista_ordenada
from pruebas import prueba_busqueda
import random

tamanos = [10, 100, 1000, 10000, 100000]

print("Tiempos de ejecución (en milisegundos) para 1000 ejecuciones:")
print("{:<10} {:<15} {:<15} {:<15}".format("Tamaño", "Lineal", "Binaria It.", "Binaria Rec."))

for tamano in tamanos:
    lista = generar_lista_ordenada(tamano)
    objetivo = random.choice(lista)

    tiempo_lineal = prueba_busqueda(busqueda_lineal, lista, objetivo)
    tiempo_iter = prueba_busqueda(busqueda_binaria_iterativa, lista, objetivo)
    tiempo_rec = prueba_busqueda(busqueda_binaria_recursiva, lista, objetivo)

    print("{:<10} {:<15.5f} {:<15.5f} {:<15.5f}".format(
        tamano, tiempo_lineal * 1000, tiempo_iter * 1000, tiempo_rec * 1000))

# Prueba adicional con objetivo inexistente
print("\nPrueba con objetivo que NO está en la lista:")
objetivo = -1
lista = generar_lista_ordenada(10000)

print("Lineal:", prueba_busqueda(busqueda_lineal, lista, objetivo) * 1000, "ms")
print("Binaria Iterativa:", prueba_busqueda(busqueda_binaria_iterativa, lista, objetivo) * 1000, "ms")
print("Binaria Recursiva:", prueba_busqueda(busqueda_binaria_recursiva, lista, objetivo) * 1000, "ms")

# Prueba con lista pequeña
print("\nResultado con lista pequeña:")
lista_pequena = [1, 2, 3]
objetivo = 2
print("Resultado búsqueda lineal:", busqueda_lineal(lista_pequena, objetivo))
print("Resultado binaria iterativa:", busqueda_binaria_iterativa(lista_pequena, objetivo))
print("Resultado binaria recursiva:", busqueda_binaria_recursiva(lista_pequena, objetivo))