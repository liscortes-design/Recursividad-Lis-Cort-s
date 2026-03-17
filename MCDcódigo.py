def calcular_mcd(na, nb):
    if nb == 0:
        return na
    else:
    
        return calcular_mcd(nb, na % nb)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultado = calcular_mcd(num1, num2)

print(f"El MCD de {num1} y {num2} es: {resultado}")