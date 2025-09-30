#Almacenar 10 notas 10, calcular la nota mayor, 
# menor, rango, mediana, moda. 
# Si la nota es mayor a 3.5 gana sino pierde, 
# una lista vacia y utilizar el metodo appeng para ingresar datos.

import statistics as stats #Libreria para hacer calculos estadisticos.
notas = [ ]

for i in range(3):
    nota = float(input("Digite la nota: "))
    notas.append(nota)

notaM = max(notas)
notaMen = min(notas)
promedio = sum(notas) / len(notas)
rango = max(notas) - min(notas)
mediana = stats.median(notas)
moda = stats.mode(notas)

print("Los resultados son:")
print(f"la nota menor es:{notaM}, la nota mayor es:{notaMen}, el promedio es igual a:{promedio}, el rango es:{rango}, La mediana es:{mediana}, La moda es:{moda},")

#Condicional
if promedio >= 3.5:
    print("Ha ganado")
else:
    print("Ha perdido")

for i,nota in enumerate(notas):
    print(f"Nota #{1+i}: {nota}")

#Un array para sumar dos vectores, multiplicacion de una lista por un escalar, multiplicar dos listas, producto punto, calcular la magnitud de un vector,de cada uno 3 ejercicios.

import numpy as np
#SUMA DE DOS VECTORES

A = np.array([1,2,3])
B = np.array([4,5,6])
C = A + B
print("suma de A y B:",C)
#En este ejercicio se crean dos vectores A y B, y se suman elemento a elemento usando A + B. El resultado es un nuevo vector C.
# Ejercicio 1
A = np.array([2, 4, 6])
B = np.array([1, 1, 1])
C = A + B
print("Suma 1:", C)

# Ejercicio 2
A = np.array([-3, 0, 5])
B = np.array([3, 7, -2])
C = A + B
print("Suma 2:", C)

# Ejercicio 3
A = np.array([0, 0, 0])
B = np.array([9, 8, 7])
C = A + B
print("Suma 3:", C)

#Multiplicación por un escalar
A = np.array([1,-2,3])
B = A * 3

print("Vectores escalado:",B)
#El vector A se multiplica por un número (escalar), en este caso 3, lo que multiplica cada componente del vector por ese número, generando un nuevo vector escalado B.
# Ejercicio 1
A = np.array([1, -1, 2])
B = A * 2
print("Escalar 1:", B)

# Ejercicio 2
A = np.array([4, 0, -3])
B = A * -1
print("Escalar 2:", B)

# Ejercicio 3
A = np.array([10, 5, -2])
B = A * 0.5
print("Escalar 3:", B)


#Producto punto

A = np.array([1,2,4])
B = np.array([4,5,6])

producto_punto = np.dot(A, B)
print("Producto punto:", producto_punto)
#Se calcula el producto punto (o producto escalar) entre los vectores A y B con np.dot(A, B). Este da como resultado un número que representa la suma de las multiplicaciones de los elementos correspondientes.
# Ejercicio 1
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
producto = np.dot(A, B)
print("Producto punto 1:", producto)

# Ejercicio 2
A = np.array([0, 1, 0])
B = np.array([7, 8, 9])
producto = np.dot(A, B)
print("Producto punto 2:", producto)

# Ejercicio 3
A = np.array([-1, 2, -3])
B = np.array([3, -2, 1])
producto = np.dot(A, B)
print("Producto punto 3:", producto)

# Magnitud de un vector

A = np.array([3, 4, 12])

magnitud = np.linalg.norm(A)
print("Magnitud de A:",magnitud)
#Se utiliza np.linalg.norm(A) para calcular la magnitud (o norma) del vector A, que representa su "tamaño" o longitud en el espacio.
import numpy as np

# Ejercicio 1
A = np.array([3, 4, 0])
magnitud = np.linalg.norm(A)
print("Magnitud 1:", magnitud)

# Ejercicio 2
A = np.array([1, 2, 2])
magnitud = np.linalg.norm(A)
print("Magnitud 2:", magnitud)

# Ejercicio 3
A = np.array([-6, -8, 0])
magnitud = np.linalg.norm(A)
print("Magnitud 3:", magnitud)
