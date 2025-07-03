agenda = []

while True:
    print("\n1.Ver\n2.Agregar\n3.Editar\n4.Salir")
    op = input("Opción: ")

    if op == "1":
        for i, c in enumerate(agenda):
            print(f"{i+1}. {c}")

    elif op == "2":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        direccion = input("Dirección: ")
        cumple = input("Cumpleaños: ")
        nota = input("Nota (máx 50): ")[:50]
        agenda.append([nombre, apellido, direccion, cumple, nota])

    elif op == "3":
        i = int(input("Número del contacto: ")) - 1
        if 0 <= i < len(agenda):
            print("Deja en blanco si no quieres cambiar algo.")
            for j, campo in enumerate(["Nombre", "Apellido", "Dirección", "Cumpleaños", "Nota"]):
                nuevo = input(f"{campo} ({agenda[i][j]}): ")
                if nuevo:
                    agenda[i][j] = nuevo[:50] if campo == "Nota" else nuevo

    elif op == "4":
        break
