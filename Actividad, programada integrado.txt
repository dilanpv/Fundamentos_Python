# Cadena de texto
cadena1 = "hola mundo,como estan?"
cadena2 = ", espero que bien."

saludo = (cadena1 + '' + cadena2)
print(saludo)
print(type(saludo))

q = 2.12
w = 1.90
h= q + w

# Suma flotante
print("RESULTADO FLOAT", h)
print(type(h))

# Suma entero
a= 10
b = 37
c = a + b
print("RESULTADO ENTERO:", c)
print(type(c))
print("\n ")


#Manipulacion de cadenas de texto:

mensaje = " Hola cusro "
# Elimina espacio al inicio y final
print(mensaje.strip())

# Convierte a mayusculas    
print("Convierte a mayusculas ",mensaje.upper())

#Reemplaza una palabra
print("Reemplaza una palabra",mensaje.replace("curso","Python"))

print("\n ")

import keyword
print(keyword.kwlist) #Muestra la lista completa de palabras reservadas
print("\n")

#Tercer ejercicio:
j = 11
l = 22

s = j + l
print("El resultado de la suma es:", s)

m = j - l
print("El resultado de la resta es:", m)

z = j * l
print("El resultado de la multiplicacion es:", z)

p = j / l
print("El resultado de la division flotante es:", p)

x = j // l
print("El resultado de la division entera es:", x)

t = j % l
print("El resultado de la modulo(residuo) es:", t)

g = j ** l
print("El resultado de la potencia es:", g)
print("\n")

nombre = input("Porfavor ingrese su nombre completo:") #Solicitamos el nombre del usuario.
welcome = print("Hola sr",nombre.upper()) # Damos la bienvenida.
edad = int(input("Cuantos años tienes:")) #Solicitamos la edad.
dias_vividos = edad * 365 #calculamos los dias vividos.
print("Usted ha vivido:",dias_vividos,"Sr",nombre.upper()) #Mostrasmos el calculo.

anos_futuros = 4
edad_futura = edad + anos_futuros #Suma
promedio_dias_anuales = dias_vividos / edad #Division
dias_vividos_dobles = dias_vividos * 2 #Multiplicacion

#Mostramos los resultados de las operaciones
print("Su edad futura sera: ",edad_futura)
print("El promedio de dias anuales es: ", promedio_dias_anuales)
print("Los dias vividos dobles es: ", dias_vividos_dobles)