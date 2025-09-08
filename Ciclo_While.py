#Ejercicio aplicando el ciclo While, Crear una variable hasta que consiga la palabra verdadera se interrumpa.
"""
palabra = " " #Almacernar.

while palabra != "salir":
    palabra = input("Ingrese la palabra: ")
    print("Digito esta palabra: ", palabra)
"""
"""
# numero mayor a 0
suma = 0
print("Ingrese el 0 para interrumpir el ciclo.")
numero = int(input("digite el numero: "))
while numero != 0:
    suma += numero
    numero = int(input("digite otro numero: "))
print("La suma de todo es: ", suma)
"""
"""
"""
opc = 0
while True:
    print("========== Bienvenidos ==========")
    print("========== Menú ==========")
    print("Opcion 1: Pescado a la plancha.")
    print("Opcion 2: Changua.")
    print("Opcion 3: Pescado a la plancha.")
    print("Seleccion una de las opciones")
    
    opc = int(input("Digite una opcion:"))
    if opc == 1:
        print("Pescado a la plancha le cuesta $50 Dollares.")
    elif opc == 2:
        print("Changua le cuesta $10 Dollares.")
    elif opc == 3:
        print("Gurre le cuesta $40 Dollares.")
    elif opc == 4:
        print("Gracias por usar el menú.")
        break
    else:
        print("Opción no válida. Intente nuevamente.") 