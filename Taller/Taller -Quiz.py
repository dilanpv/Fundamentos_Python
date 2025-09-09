# # # 1.	Variables y tipos de datos
# # #	Solicita el nombre del estudiante (cadena).
# # nombre = input("Ingrese su nombre:")
# # print("su nombre es: ",nombre)
# # # 	Solicita su edad (entero).
# # print("\n")
# edad = int(input("Digite su edad: "))
# # # print("La edad ingresada es:",edad)
# # # print("\n")
# # # # 	Solicita la nota promedio del último semestre (decimal).
# nota = float(input("Digite su nota promedio del ultimo semestre:"))
# # # print("La nota ingresada es: ",nota)
# # # print("\n")
# # # # 	Muestra en pantalla un mensaje de bienvenida con todos los datos ingresados.
# # # print("\n")
# # #=============================================================================================
# # 2.	Condicionales
# #Si la edad es menor a 18, mostrar "Eres menor de edad", de lo contrario "Eres mayor de edad".
# if edad <18 :
#     print("Eres menor de edad")
# else:
#     print("Eres mayor de edad")
# #Si la nota promedio es mayor o igual a 3.0 mostrar "Aprobaste", de lo contrario "Reprobaste".
# if nota >= 3.0:
#     print("Aprobaste")
# else:
#     print("Reprobaste")
# print("\n")
# #==============================================================================================
# # 3.	Ciclo for
# #Pide un número entero n.
# num = int(input("Digite el numero a multiplicar:"))
# for i in range(1, 11):
#     print("Resultado:",i*num)
#Muestra la tabla de multiplicar de ese número del 1 al 10.
#==============================================================================================
# 4.	Ciclo while
# Crea un pequeño juego donde el estudiante debe adivinar un número secreto entre 1 y 5.
adivinar= 0
secreto = 4
while adivinar != secreto :
    adivinar = int(input("Digite el numero a adivinar: "))
    if adivinar == secreto:
        print("Correcto")
# El programa debe seguir preguntando hasta que lo adivine.
# Cuando lo logre, mostrar "¡Correcto!".
