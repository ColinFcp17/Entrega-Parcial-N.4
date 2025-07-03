estudiantes = []
asignaturas = {
    "Ingenieria": ["Móvil", "Web", "Escritorio"],
    "Analista": ["Análisis", "Limpieza", "Dashboard"],
    "Gastronomia": ["Historia", "Naturales", "Procesados"]
}

while True:
    op = input("\n1.Agregar \n2.Ver \n3.Asignaturas \n4.Salir: ")
    op = input("Seleccione una Opcion: ")

    if op == "1":
        nom = input("Nombre: ")
        ape = input("Apellido: ")
        rut = input("RUT: ")
        mail = input("Correo: ")
        car = input("Carrera (Ingenieria, Analista, Gastronomia): ").capitalize()
        if car in asignaturas:
            estudiantes.append([nom, ape, rut, mail, car])
        else:
            print("Carrera no válida.")

    elif op == "2":
        for e in estudiantes:
            print(f"{e[0]} {e[1]} | {e[2]} | {e[3]} | {e[4]}")

    elif op == "3":
        for c, a in asignaturas.items():
            print(f"{c}: {', '.join(a)}")

    elif op == "4":
        break
