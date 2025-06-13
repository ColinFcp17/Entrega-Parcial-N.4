usuarios = {}

while True:
    print("\n1. Ingresar\n2. Buscar\n3. Eliminar\n4. Salir")
    op = input("Opción: ")

    if op == '1':
        nombre = input("Nombre: ")
        if nombre in usuarios:
            print("Ya existe.")
            continue
        sexo = input("Sexo (M/F): ")
        clave = input("Clave: ")
        usuarios[nombre] = (sexo, clave)
        print("Usuario guardado.")

    elif op == '2':
        nombre = input("Nombre a buscar: ")
        if nombre in usuarios:
            print("Sexo:", usuarios[nombre][0])
            print("Clave:", usuarios[nombre][1])
        else:
            print("No encontrado.")

    elif op == '3':
        nombre = input("Nombre a eliminar: ")
        if nombre in usuarios:
            del usuarios[nombre]
            print("Eliminado.")
        else:
            print("No existe.")

    elif op == '4':
        break
    else:
        print("Opción inválida.")