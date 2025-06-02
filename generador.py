import random

def generar_lista_ordenada(tamano):
    return sorted(random.sample(range(tamano*10), tamano))
