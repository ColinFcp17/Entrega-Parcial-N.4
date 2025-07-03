usuarios = {}

def ingresar():
    nombre = input("Nombre: ")
    if nombre in usuarios:
        print("Ya existe.")
        return
    sexo = input("Sexo (F/M): ")
    clave = input("Clave: ")
    usuarios[nombre] = [sexo, clave]
    print("Ingreso exitoso.")

def buscar():
    nombre = input("Buscar: ")
    if nombre in usuarios:
        print("Sexo:", usuarios[nombre][0], "| Clave:", usuarios[nombre][1])
    else:
        print("No registrado.")

def eliminar():
    nombre = input("Eliminar: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print("Eliminado.")
    else:
        print("No registrado.")

def main():
    while True:
        print("\n1.Ingresar 2.Buscar 3.Eliminar 4.Salir")
        op = input("Opción: ")
        if op == "1": ingresar()
        elif op == "2": buscar()
        elif op == "3": eliminar()
        elif op == "4": break
        else: print("Opción inválida.")

main()
