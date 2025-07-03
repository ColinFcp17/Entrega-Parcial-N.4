compradores = {}
stock = {"1": 25, "2": 25}

def vender():
    if sum(stock.values()) == 0: return print("Entradas agotadas.")
    nom = input("Nombre: ")
    if nom in compradores: return print("Nombre repetido.")
    s = input("Función (1: Tripulación / 2: Sonrisas): ")
    if s in stock and stock[s] > 0:
        compradores[nom], stock[s] = s, stock[s] - 1
        print("Entrada registrada.")
    else:
        print("Función inválida o sin cupo.")

def cambiar():
    nom = input("Nombre: ")
    if nom not in compradores: return print("No registrado.")
    act, nueva = compradores[nom], "2" if compradores[nom] == "1" else "1"
    if stock[nueva] > 0:
        compradores[nom], stock[act], stock[nueva] = nueva, stock[act]+1, stock[nueva]-1
        print("Cambio realizado.")
    else:
        print("Sin cupo en otra función.")

def mostrar(): print(f"Stock -> Función 1: {stock['1']}, Función 2: {stock['2']}")

def main():
    while True:
        op = input("\n1.Venta 2.Cambio 3.Stock 4.Salir: ")
        if op == "1": vender()
        elif op == "2": cambiar()
        elif op == "3": mostrar()
        elif op == "4": break
        else: print("Opción inválida.")

main()
