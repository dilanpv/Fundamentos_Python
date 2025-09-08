#Basicas:
#if =>  Verifica que la condicion sea verdadera.
#if else => Primero ejecuta el if y luego pasa al else.
#elif =>    Cuando tenemos multiples condiciones verdadera.

#Ejercicio
numero = int(input("Digite un numero entero:"))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

#Programa que identifica que una persona sea mayor de edad:

edad = int(input("Ingrese la edad"))

if edad >= 18:
    print("Eres mayor de edad...", edad)
else:
    print("Eres menor de edad :(", edad)

#Programa que culcule que si un numero es positivo, negativo o cero

num = float(input("Ingrese el numero a revisar"))
if num > 0:
    print("El numero es positivo")
elif num<0:
    print("El numero es negativo")
    
else:
    print("El numero es netro")

#Programa que califeque notas, 
# donde la nota entre 0 y 2.9 perdio, 
# 3.0 a 3.9 es aprobado, 
# 4.0 a 4.5 es sobresalientes,
# 4.6 a 5.0 excelente, 
# sino nota fuera de los rangos.
nota = float(input("Digite la nota: "))

if nota >= 0 and nota <= 2.9:
    print("Perdio")
elif nota >= 3.0 and nota <= 3.9:
    print("Aprobado")
elif nota >= 4.0 and nota <= 4.5:
    print("Sobresaliente")
elif nota >= 4.6 and nota <= 5.0:
    print("excelente")
else:
    print("Nota fuera de rango...")
    
#Programa para indicar la temperatura.
tempetatura = int(input("Digite la temperatura actual: "))
if tempetatura >= 36 and tempetatura <= 37:
    print("Temperatura normal. :)")
    
elif tempetatura >= 37 and tempetatura <= 54:
    print("Deshidratacion beber agua porfavor.")
    
elif tempetatura >= 55 and tempetatura <= 70:
    print("Temperatura máxima, CUIDADO.")
    
else:
    print("Temperatura fuera de rango...")