#Programa para saber si un estudiante aplica a una beca o matricula gratis: 16 a 25 años, 
# promedio de 4 en adelante y 
# debe ser del estrato 1,2 o 3 
# debe ser de la universidad Luis amigó.

edad = int(input("Ingrese la edad: "))
promedio = float(input("Ingrese su promedio: "))
estrato = int(input("Ingrese su estrato: "))

#Utilizamos los operadores logicos
if (edad >= 16 and edad <= 25) and (promedio >= 4.0) and (estrato <4):
    print("SE GANÓ LA BECA")
else:
    print("No cumple los requisitos, sorry.")


