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
    
#función lineal, busqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1





    

