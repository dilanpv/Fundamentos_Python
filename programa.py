
# ====== PROGRAMA FINAL ======
print("=== PROGRAMA FINAL ===")
nombre = input("Escribe tu nombre: ")
print("¡Hola", nombre.upper(), "!")

# Pedir edad de forma sencilla
edad = int(input("¿Cuántos años tienes? "))

# Cálculos
dias = edad * 365
meses = edad * 12
semanas = dias // 7
horas = dias * 24

print(nombre, "has vivido aprox.", dias, "días.")
print("Eso es como", horas, "horas y", semanas, "semanas.")
print()

# Ver tipos
print("Tipos de datos:")
print("nombre:", type(nombre))
print("edad:", type(edad))
print("dias:", type(dias))
print()

print("Fin del programa :)")