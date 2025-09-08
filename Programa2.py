# -------------------------------------------------
# CONDICIONALES Y OPERADORES EN PYTHON
# -------------------------------------------------

# Condicionales:
#   Qué son: estructuras que permiten ejecutar distintas instrucciones según si
#   una o varias condiciones se cumplen.
#   Para qué se utilizan: tomar decisiones en el flujo del programa (ej. validar datos,
#   elegir entre alternativas, manejar errores o rutas de ejecución).
#
# Operadores Relacionales:
#   Qué son: comparan valores y devuelven True o False (==, !=, >, <, >=, <=).
#   Para qué se utilizan: verificar relaciones entre datos (ej. si una edad es mayor a 18,
#   si dos cadenas son iguales, si un número está por encima de un umbral).
#
# Operadores Lógicos:
#   Qué son: combinan expresiones booleanas (and, or, not).
#   Para qué se utilizan: construir condiciones más complejas (ej. "si A y B son verdaderas",
#   "si no se cumple X", o "si A o B es verdadera") para afinar decisiones.
#
# Operadores de Pertenencia:
#   Qué son: comprueban si un elemento pertenece o no a una colección (in, not in).
#   Para qué se utilizan: verificar existencia dentro de listas/tuplas/sets/strings o comprobar
#   si una clave está en un diccionario (ej. validar si un usuario está en la lista de permitidos).
# -------------------------------------------------

print("\n MENÚ DE EJEMPLOS DE OPERADORES EN PYTHON")
print("1 - Operadores Relacionales (2 ejemplos)")
print("2 - Operadores Lógicos (4 ejemplos)")
print("3 - Operadores de Pertenencia (6 ejemplos)")
print("0 - Salir\n")

op = input("Elige una opción: ")

# ----------------------------------------
# RELACIONALES
# ----------------------------------------
if op == "1":
    print("\n🔹 Operadores Relacionales:")
    edad = int(input("¿Cuál es tu edad? "))
    if edad >= 18:
        print("Ejemplo 1: ",edad," >= 18 ->", edad >= 18, "eres mayor de edad")
    else:
        print("Ejemplo 1: ",edad," >= 18 ->", edad >= 18, "eres menor de edad")

    num1 = int(input("Ingresa un número: "))
    num2 = int(input("Ingresa otro número: "))
    print("Ejemplo 2: ",num1," == ",num2,"->", num1 == num2)

# ----------------------------------------
# LÓGICOS
# ----------------------------------------
elif op == "2":
    print("\n🔹 Operadores Lógicos:")
    tiene_dinero = input("¿Tienes dinero? (si/no): ") == "si"
    tiene_tiquete = input("¿Tienes tiquete? (si/no): ") == "si"

    print("Ejemplo 1: (dinero AND tiquete) ->", tiene_dinero and tiene_tiquete)
    print("   (Puedes viajar solo si tienes ambas cosas)")
    print("\n")
    clima = input("¿Está soleado? (si/no): ") == "si"
    sombrilla = input("¿Llevas sombrilla? (si/no): ") == "si"

    print("Ejemplo 2: (soleado OR sombrilla) ->", clima or sombrilla)
    print("\n")
    
    hambre = input("¿Tienes hambre? (si/no): ") == "si"
    print("Ejemplo 3: not(hambre) ->", not hambre)
    print("\n")
    estudiar = input("¿Quieres estudiar hoy? (si/no): ") == "si"
    cansado = input("¿Estás cansado? (si/no): ") == "si"
    print("Ejemplo 4: estudiar AND not(cansado) ->", estudiar and not cansado)

# ----------------------------------------
# PERTENENCIA
# ----------------------------------------
elif op == "3":
    print("\n🔹 Operadores de Pertenencia:")

    lista_usuarios = ["ana", "luis", "carlos", "maria"]
    print("Lista de usuarios -> ",lista_usuarios)
    usuario = input("Escribe tu nombre: ")
    print("Ejemplo 1:", usuario, "in lista_usuarios ->", usuario in lista_usuarios)
    print("\n")
    
    print("Buscar la letra 'a', en una palabra: ")
    palabra = input("Escribe una palabra: ")
    print("Ejemplo 2: 'a' in palabra ->", "a" in palabra)
    print("\n")

    numeros = [1, 2, 3, 4, 5]
    print("Lista de numeros -> ",numeros)
    n = int(input("Escribe un número: "))
    print("Ejemplo 3:", n, "in numeros ->", n in numeros)
    print("\n")

    frutas = ["manzana", "pera", "uva"]
    print("Lista de frutas -> ",frutas)
    fruta = input("Escribe una fruta: ")
    print("Ejemplo 4:", fruta, "not in frutas ->", fruta not in frutas)
    print("\n")

    texto = "python es divertido, las clases son agradables"
    print("Este es el texto asignado -> ", texto)
    sub = input("Escribe una letra o palabra para buscar en el texto: ")
    print("Ejemplo 5:", sub, "in texto ->", sub in texto)
    print("\n")

    letras = "aeiou"
    print("Estas son las letras asignadas -> ", letras)
    letra = input("Escribe una letra: ")
    print("Ejemplo 6:", letra, "in vocales ->", letra in letras)

# ----------------------------------------
# SALIR
# ----------------------------------------
elif op == "0":
    print("\nSaliendo...")
else:
    print("\nOpción no válida, elige 0, 1, 2 o 3.")
    