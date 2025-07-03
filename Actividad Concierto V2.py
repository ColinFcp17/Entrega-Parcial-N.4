compradores = {}

def comprar():
    nombre = input("Nombre: ")
    if nombre in compradores:
        print("Ya existe.")
        return
    tipo = input("Tipo (General/VIP): ").strip().lower()
    if tipo not in ["general", "vip"]:
        print("Tipo inválido.")
        return
    codigo = input("Código: ")
    compradores[nombre] = [tipo.upper(), codigo]
    print("Compra registrada.")

def consultar():
    nombre = input("Buscar nombre: ")
    if nombre in compradores:
        print("Tipo:", compradores[nombre][0])
        print("Código:", compradores[nombre][1])
    else:
        print("No existe.")

def cancelar():
    nombre = input("Eliminar: ")
    if nombre in compradores:
        del compradores[nombre]
        print("Eliminado.")
    else:
        print("No existe.")

def main():
    while True:
        print("\n1.Comprar\n2.Consultar\n3.Cancelar\n4.Salir")
        op = input("Opción: ")
        if op == "1": comprar()
        elif op == "2": consultar()
        elif op == "3": cancelar()
        elif op == "4": break
        else: print("Opción inválida.")

main()
