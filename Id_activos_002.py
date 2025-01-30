import csv

# Base de datos simulada de activos
activos = []

# Niveles de criticidad
niveles = {
    "B": 1,  # Bajo
    "M": 2,  # Medio
    "A": 3,  # Alto
}

# Función para agregar activos
def agregar_activo():
    id_activo = input("ID del Activo: ")
    nombre = input("Nombre del Activo: ")
    propietario = input("Propietario: ")
    ubicacion = input("Ubicación (Local/Nube/Data Center): ")
    
    print("\nEvaluación CIA (Confidencialidad, Integridad, Disponibilidad)")
    confidencialidad = input("Confidencialidad (B/M/A): ").upper()
    integridad = input("Integridad (B/M/A): ").upper()
    disponibilidad = input("Disponibilidad (B/M/A): ").upper()
    
    # Validar entradas
    if confidencialidad not in niveles or integridad not in niveles or disponibilidad not in niveles:
        print("Error: Debe ingresar B, M o A en los valores CIA.")
        return
    
    # Calcular criticidad
    criticidad = niveles[confidencialidad] + niveles[integridad] + niveles[disponibilidad]

    if criticidad >= 8:
        riesgo = "ALTO"
    elif criticidad >= 5:
        riesgo = "MEDIO"
    else:
        riesgo = "BAJO"
    
    # Guardar activo
    activos.append([id_activo, nombre, propietario, ubicacion, confidencialidad, integridad, disponibilidad, riesgo])
    print("\nActivo registrado con éxito!")

# Función para mostrar activos
def mostrar_activos():
    if not activos:
        print("\nNo hay activos registrados.")
        return
    
    print("\nLista de Activos registrados:")
    print("ID | Nombre | Propietario | Ubicación | Confidencialidad | Integridad | Disponibilidad | Riesgo")
    print("-" * 90)
    for a in activos:
        print(f"{a[0]} | {a[1]} | {a[2]} | {a[3]} | {a[4]} | {a[5]} | {a[6]} | {a[7]}")

# Función para exportar a CSV
def exportar_csv():
    with open("activos_sgsi.csv", "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["ID", "Nombre", "Propietario", "Ubicación", "Confidencialidad", "Integridad", "Disponibilidad", "Riesgo"])
        writer.writerows(activos)
    print("\nArchivo ‘activos_sgsi.csv’ exportado con éxito!")

# Menú principal
while True:
    print("\n=== GESTIÓN DE ACTIVOS SGSI - ISO 27001 ===")
    print("1. Agregar activo")
    print("2. Mostrar activos")
    print("3. Exportar a CSV")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_activo()
    elif opcion == "2":
        mostrar_activos()
    elif opcion == "3":
        exportar_csv()
    elif opcion == "4":
        print("\nSaliendo del Programa...")
        break
    else:
        print("\nOpción inválida. Intente nuevamente.")