def busqueda_binaria_iterativa(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        
        if lista[medio] == objetivo:
            return medio  # Encontró el valor, retorna índice
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    return None  # No se encontró el valor


def busqueda_binaria_recursiva(lista, objetivo, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1

    if inicio > fin:
        return -1  # Valor no encontrado

    medio = (inicio + fin) // 2

    if lista[medio] == objetivo:
        return medio  # Se encontró el valor

    elif lista[medio] < objetivo:
        # Buscar en la mitad derecha
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, fin)
    else:
        # Buscar en la mitad izquierda
        return busqueda_binaria_recursiva(lista, objetivo, inicio, medio - 1)
    
#Implementación de prueba 
import timeit
import random

def generar_lista_ordenada(tamano):
    return sorted(random.sample(range(tamano*10), tamano))

def prueba_busqueda(funcion, lista, objetivo):
    # Usamos timeit para medir el tiempo
    tiempo = timeit.timeit(lambda: funcion(lista, objetivo), number=1000)
    return tiempo

# Tamaños de lista para probar
tamanos = [10, 100, 1000, 10000, 100000, 1000000]

print("Tiempos de ejecución (en milisegundos) para 1000 ejecuciones:")
print("{:<10} {:<20} {:<20}".format("Tamaño", "Iterativa", "Recursiva"))

for tamano in tamanos:
    lista = generar_lista_ordenada(tamano)
    objetivo = random.choice(lista)  # Objetivo que existe en la lista
    
    # Probamos con un objetivo que existe
    tiempo_iter = prueba_busqueda(busqueda_binaria_iterativa, lista, objetivo)
    tiempo_rec = prueba_busqueda(busqueda_binaria_recursiva, lista, objetivo)
    
    print("{:<10} {:<20.5f} {:<20.5f}".format(
        tamano, tiempo_iter*1000, tiempo_rec*1000))
    

#Prueba adicional 

# Prueba con objetivo no existente
objetivo = -1  # Que no existe en la lista
tiempo_iter = prueba_busqueda(busqueda_binaria_iterativa, lista, objetivo)
tiempo_rec = prueba_busqueda(busqueda_binaria_recursiva, lista, objetivo)

# Prueba con listas pequeñas (caso base)
lista_pequena = [1, 2, 3]
objetivo = 2

    

