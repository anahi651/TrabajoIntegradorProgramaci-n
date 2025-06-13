# main.py
from empleados import (
    ingresar_empleados,
    agregar_empleados,
    mostrar_empleados,
    ordenar_por_salario,
    buscar_empleados_por_edad,
    busqueda_lineal_por_apellido
)

def main():
    print("GESTIÓN DE EMPLEADOS")

    respuesta = input("¿Querés agregar nuevos empleados? (s/n): ").lower()
    if respuesta == 's':
        agregar_empleados()

    empleados = ingresar_empleados()

    print("\n Lista actual de empleados:")
    mostrar_empleados(empleados)

    print("\n Empleados ordenados por salario (descendente):")
    empleados_ordenados = ordenar_por_salario(empleados)
    mostrar_empleados(empleados_ordenados)

    print("\n Buscar empleados por rango de edad:")
    buscar_empleados_por_edad(empleados)

    print("\n Buscar por apellido:")
    apellido = input("Ingrese el apellido a buscar: ")
    encontrado = busqueda_lineal_por_apellido(empleados, apellido)
    if encontrado:
        print(f"Empleado encontrado: {encontrado['nombre']} {encontrado['apellido']}, Salario: ${encontrado['salario']}")
    else:
        print("No se encontró un empleado con ese apellido.")

if __name__ == "__main__":
    main()
