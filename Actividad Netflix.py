peliculas = []

def main():
    while True:
        print("\n1.Añadir película\n2.Tipo\n3.Duración\n4.Salir")
        op = input("Opción: ")

        if op == "1":
            nombre = input("Nombre: ")
            peliculas.append([nombre, "", ""])
            print("Película añadida.")
        elif op == "2":
            if peliculas:
                tipo = input("Tipo: ")
                peliculas[-1][1] = tipo
        elif op == "3":
            if peliculas:
                duracion = input("Duración: ")
                peliculas[-1][2] = duracion
        elif op == "4":
            for p in peliculas:
                print(f"{p[0]} | {p[1]} | {p[2]} min")
            break
        else:
            print("Opción inválida.")

main()
