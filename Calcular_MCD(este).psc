Algoritmo Calcular_MCD
	Definir na, nb, resultado Como Entero
	Escribir 'Ingrese el primer número: '
	Leer na
	Escribir 'Ingrese el segundo número: '
	Leer nb
	resultado <- MCD(na,nb)
	Escribir 'El MCD de ', na, ' y ', nb, ' es: ', resultado
FinAlgoritmo

Función res <- MCD(a,b)
	Si b=0 Entonces
		res <- a
	SiNo
		res <- MCD(b,a MOD b)
	FinSi
FinFunción
