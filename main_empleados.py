# main.py

# Importa las funciones necesarias desde el módulo empleados
from empleados import (
    ingresar_empleados,
    agregar_empleados,
    mostrar_empleados,
    ordenar_por_salario,
    buscar_empleados_por_edad,
    busqueda_lineal_por_apellido
)

def main():
    """
    Función principal que ejecuta el flujo del programa para gestionar empleados:
    - Permite agregar nuevos empleados si el usuario lo desea.
    - Permite ingresar empleados.
    - Muestra la lista actual de empleados.
    - Muestra la lista de empleados ordenada por salario en forma descendente.
    - Permite buscar empleados por rango de edad.
    - Permite buscar un empleado por apellido utilizando búsqueda lineal.
    """

    print("GESTIÓN DE EMPLEADOS")

    # Pregunta al usuario si quiere agregar nuevos empleados
    respuesta = input("¿Querés agregar nuevos empleados? (s/n): ").lower()
    if respuesta == 's':
        agregar_empleados()  # Llama a la función para agregar empleados

    # Solicita ingresar empleados y almacena la lista resultante
    empleados = ingresar_empleados()

    # Muestra la lista completa de empleados ingresados
    print("\n Lista actual de empleados:")
    mostrar_empleados(empleados)

    # Ordena y muestra los empleados según su salario, de mayor a menor
    print("\n Empleados ordenados por salario (descendente):")
    empleados_ordenados = ordenar_por_salario(empleados)
    mostrar_empleados(empleados_ordenados)

    # Invita al usuario a buscar empleados por rango de edad
    print("\n Buscar empleados por rango de edad:")
    buscar_empleados_por_edad(empleados)

    # Busca un empleado por apellido usando búsqueda lineal
    print("\n Buscar por apellido:")
    apellido = input("Ingrese el apellido a buscar: ")
    encontrado = busqueda_lineal_por_apellido(empleados, apellido)
    
    if encontrado:
        # Si se encuentra, muestra datos del empleado
        print(f"Empleado encontrado: {encontrado['nombre']} {encontrado['apellido']}, Salario: ${encontrado['salario']}")
    else:
        # Si no se encuentra, informa al usuario
        print("No se encontró un empleado con ese apellido.")

# Punto de entrada principal del script
if __name__ == "__main__":
    main()
