def calcular_mcd(na, nb):
    if nb == 0:
        return na
    else:
    
        return calcular_mcd(nb, na % nb)

na = int(input("Ingrese el primer número: "))
nb = int(input("Ingrese el segundo número: "))
resultado = calcular_mcd(na, nb)

print(f"El MCD de {na} y {nb} es: {resultado}")

