def validar_rut_simple(rut):
    if "-" not in rut:
        return False
    num, dv = rut.split("-")
    return num.isdigit() and len(num) <= 8 and len(dv) == 1

def validar_comuna(c):
    comunas = ["CERRILLOS","CERRO NAVIA","CONCHALI","EL BOSQUE","ESTACION CENTRAL","HUECHURABA",
    "INDEPENDENCIA","LA CISTERNA","LA FLORIDA","LA GRANJA","LA PINTANA","LA REINA","LAS CONDES",
    "LO BARNECHEA","LO ESPEJO","LO PRADO","MACUL","MAIPU","NUNOA","PAINE","PEDRO AGUIRRE CERDA",
    "PEÑALOLEN","PROVIDENCIA","PUDAHUEL","QUILICURA","QUINTA NORMAL","RECOLETA","RENCA",
    "SAN JOAQUIN","SAN MIGUEL","SAN RAMON","SANTIAGO","VITACURA"]
    return c.upper() in comunas

def main():
    rut = input("Ingrese RUT (formato 12345678-9): ")
    if not validar_rut_simple(rut):
        print("RUT inválido.")
        return
    nombre = input("Nombre y apellido: ")
    print("1.Heridas 2.Virus 3.Hemorragias 4.Alergias 5.Deshidratación")
    patologia = input("Patología (1-5): ")
    comuna = input("Comuna: ")
    if not validar_comuna(comuna):
        print("Paciente no corresponde a la región metropolitana.")
        return
    
    print("\n--- Datos ingresados ---")
    print(f"RUT: {rut}")
    print(f"Nombre: {nombre}")
    print(f"Patología: {patologia}")
    print(f"Comuna: {comuna}")

main()


