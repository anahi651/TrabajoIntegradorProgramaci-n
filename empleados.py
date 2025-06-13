# empleados.py
import csv

def ingresar_empleados():
    """
    Lee los empleados desde un archivo CSV y devuelve una lista de diccionarios.
    """
    empleados = []
    with open('empleados.csv', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            empleados.append({
                "nombre": fila["nombre"],
                "apellido": fila["apellido"],
                "edad": int(fila["edad"]),
                "salario": float(fila["salario"])
            })
    return empleados

def agregar_empleados():
    """
    Permite agregar nuevos empleados por teclado y los guarda en empleados.csv.
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
    Muestra una lista de empleados en formato legible.
    """
    for emp in empleados:
        print(f"{emp['nombre']} {emp['apellido']} - Edad: {emp['edad']}, Salario: ${emp['salario']:,.2f}")

def ordenar_por_salario(empleados):
    return sorted(empleados, key=lambda emp: emp["salario"], reverse=True)

def buscar_empleados_por_edad(empleados):
    edad_min = int(input("Edad mínima: "))
    edad_max = int(input("Edad máxima: "))
    resultados = [emp for emp in empleados if edad_min <= emp["edad"] <= edad_max]

    if resultados:
        print(f"\nEmpleados entre {edad_min} y {edad_max} años:")
        mostrar_empleados(resultados)
    else:
        print("No se encontraron empleados en ese rango.")

def busqueda_lineal_por_apellido(empleados, apellido):
    for emp in empleados:
        if emp["apellido"].lower() == apellido.lower():
            return emp
    return None
