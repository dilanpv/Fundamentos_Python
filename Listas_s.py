# Ejemplos de listas en Python

# INDEXACION
# Sirve para acceder a los elementos de la lista usando posiciones

numeros = [10, 20, 30, 40, 50]

print("Indexacion ejemplos:")
print(numeros[0])   # primer elemento
print(numeros[2])   # tercer elemento
print(numeros[-1])  # ultimo elemento
print(numeros[1:4]) # del indice 1 al 3
print(numeros[:3])  # primeros tres
print()

# METODOS DE LISTAS

# remove(valor) elimina el primer valor que encuentre
frutas = ["manzana", "pera", "uva", "pera"]
frutas.remove("pera")
print("remove:", frutas)

# pop() elimina un elemento por indice, si no se pone indice elimina el ultimo
nums = [1, 2, 3, 4]
nums.pop(2)  # elimina el 3
print("pop:", nums)

# append() agrega un elemento al final
animales = ["perro", "gato"]
animales.append("loro")
print("append:", animales)
print()

# EDITAR ELEMENTO
# Se cambia un valor usando su posicion
colores = ["rojo", "verde", "azul"]
colores[1] = "amarillo"
print("editar:", colores)
print()

# insert()
# Inserta un elemento en la posicion indicada
nombres = ["Ana", "Luis", "Carlos"]
nombres.insert(1, "Pedro")
print("insert:", nombres)
print()

# extend()
# Une dos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print("extend:", lista1)
print()

# EJERCICIO 1
numeros = [1, 2, 3, 4, 5]
numeros.extend([6, 7, 8, 9, 10])  # agregar mas
numeros.insert(1, 99)             # insertar en posicion 2
numeros.pop(0)                    # borrar primer elemento
numeros.remove(8)                 # borrar el 8
numeros[-1] = 0                   # cambiar ultimo por 0

print("ejercicio 1:", numeros)
print()

# EJERCICIO 2
companeros = ["Yamit", "Dilan", "Carlos", "Chaverra"]
nuevo = "Johan"
companeros.append(nuevo)

# iniciales con la primera letra de cada nombre
iniciales = "".join([nombre[0] for nombre in companeros])
print("companeros:", companeros)
print("iniciales:", iniciales)
print()

# EJERCICIO LIBRE
compras = ["arroz", "leche", "pan", "huevos"]
producto = "queso"

if producto in compras:
    print(producto, "ya esta en la lista")
else:
    print(producto, "no esta en la lista se agrega")
    compras.append(producto)

print("compras:", compras)
