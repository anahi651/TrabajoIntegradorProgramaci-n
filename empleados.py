import csv

def ingresar_empleados():
    """
    Lee los empleados desde el archivo 'empleados.csv' y los devuelve como una lista de diccionarios.

    Cada diccionario representa un empleado con las claves: nombre, apellido, edad y salario.

    Retorna:
    - Lista de empleados (diccionarios).
    """
    empleados = []
    try:
        with open('empleados.csv', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                empleados.append({
                    "nombre": fila["nombre"],
                    "apellido": fila["apellido"],
                    "edad": int(fila["edad"]),
                    "salario": float(fila["salario"])
                })
    except FileNotFoundError:
        print(" Archivo 'empleados.csv' no encontrado. Se usará una lista vacía.")
    return empleados


def agregar_empleados():
    """
    Permite ingresar empleados manualmente desde el teclado.
    Guarda los datos ingresados en el archivo 'empleados.csv' (modo append).
    """
    cantidad = int(input("¿Cuántos empleados nuevos deseas agregar? "))

    with open('empleados.csv', 'a', newline='', encoding='utf-8') as archivo:
        campos = ['nombre', 'apellido', 'edad', 'salario']
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        for i in range(cantidad):
            print(f"\nIngrese datos del empleado {i + 1}:")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: "))
            salario = float(input("Salario: "))

            escritor.writerow({
                'nombre': nombre,
                'apellido': apellido,
                'edad': edad,
                'salario': salario
            })

    print("\n Empleados agregados correctamente.")


def mostrar_empleados(empleados):
    """
    Muestra una lista de empleados por consola de forma legible.

    Parámetro:
    - empleados: lista de diccionarios con los datos de cada empleado.
    """
    for emp in empleados:
        print(f"{emp['nombre']} {emp['apellido']} - Edad: {emp['edad']}, Salario: ${emp['salario']:,.2f}")


def ordenar_por_salario(empleados):
    """
    Ordena la lista de empleados de forma descendente según el salario.

    Parámetro:
    - empleados: lista de empleados

    Retorna:
    - Nueva lista ordenada por salario (mayor a menor)
    """
    return sorted(empleados, key=lambda emp: emp["salario"], reverse=True)


def buscar_empleados_por_edad(empleados):
    """
    Filtra empleados que están dentro de un rango de edad indicado por el usuario.
    Muestra los resultados por pantalla.

    Parámetro:
    - empleados: lista de empleados
    """
    edad_min = int(input("Edad mínima: "))
    edad_max = int(input("Edad máxima: "))
    resultados = [emp for emp in empleados if edad_min <= emp["edad"] <= edad_max]

    if resultados:
        print(f"\nEmpleados entre {edad_min} y {edad_max} años:")
        mostrar_empleados(resultados)
    else:
        print("No se encontraron empleados en ese rango de edad.")


def busqueda_lineal_por_apellido(empleados, apellido):
    """
    Busca un empleado en la lista comparando el apellido uno por uno (búsqueda lineal).

    Parámetros:
    - empleados: lista de empleados
    - apellido: string a buscar (no distingue mayúsculas/minúsculas)

    Retorna:
    - El diccionario del empleado encontrado o None si no existe.
    """
    for emp in empleados:
        if emp["apellido"].lower() == apellido.lower():
            return emp
    return None
