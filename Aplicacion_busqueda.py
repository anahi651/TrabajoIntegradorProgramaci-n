# Aplicaciìn de busqueda y ordenamiento
# Realizar un programa donde el usuario pueda ingrresar a sus empleados, con nombre 
# apellido, edad y salario y pueda ordenarlos y buscarlos.

# Función para ingresar datos de empleados
def ingresar_empleados():
    empleados = []
    cantidad = int(input("¿Cuántos empleados deseas ingresar? "))
    for i in range(cantidad):
        print(f"\nIngrese datos del empleado {i + 1}:")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        salario = float(input("Salario: "))
        empleados.append({
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "salario": salario
        })
    return empleados

# Función para mostrar los empleados
def mostrar_empleados(empleados):
    for emp in empleados:
        print(f"{emp['nombre']} {emp['apellido']} - Edad: {emp['edad']}, Salario: ${emp['salario']}")

# Función para ordenar por salario
def ordenar_por_salario(empleados):
    return sorted(empleados, key=lambda emp: emp["salario"], reverse=True)

# Función para buscar empleados por rango de edad
def buscar_empleados_por_edad(empleados):
    edad_min = int(input("Edad mínima: "))
    edad_max = int(input("Edad máxima: "))
    resultados = [
        emp for emp in empleados
        if edad_min <= emp["edad"] <= edad_max
    ]
    if resultados:
        print(f"\nEmpleados con edades entre {edad_min} y {edad_max}:")
        mostrar_empleados(resultados)
    else:
        print("No se encontraron empleados en ese rango de edad.")

# Programa principal
def main():
    empleados = ingresar_empleados()

    print("\nLista de empleados ingresados:")
    mostrar_empleados(empleados)

    empleados_ordenados = ordenar_por_salario(empleados)
    print("\nEmpleados ordenados por salario (descendente):")
    mostrar_empleados(empleados_ordenados)

    print("\nBuscar empleados por rango de edad:")
    buscar_empleados_por_edad(empleados)

if __name__ == "__main__":
    main()