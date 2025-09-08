import statistics
#Ciclo que recorra mi nombre.
"""
nombre = input("Ingrese el nombre: ")
vocales = "aeiouAEIOU"
contador = 0 

for run in nombre:
    if run in vocales:
        contador += 1
print("Canrtidad: ",contador)
"""
"""
palabras = ["Hola", "conejo", "sapo",1]
for pal in range(0,len(palabras)):
    print("Palabras de la lista: ",palabras[pal])
print (type(palabras[3]))
"""
#Cree un programa con una lista vacia para guardar 20 notas de los estudiantes de español de la Universidad,
#utilizar el ciclo for para mostrar cada nota con su respectivo numero de estudiantes,
#al final calcular el promedio, la nota mas alta, mas baja y la mas repetida de la lista.(leg - range)

notas = []
promedio = 0
for i in range(5):
    nota = float(input(f"Digite la nota: {i+1}:"))
    notas.append(nota)
    print("Notas almacenadas.")
print("\n")

for i  in range(len(notas)):
    print(f"estudiante  {i+1}: {notas[i]}") 
    promedio = sum(notas)/len(notas)
    print("El promedio es igual a: ",promedio)

print("\n")
notamax = max(notas)
print("La nota mas alta es: ",notamax)

print("\n")
notamin = min(notas)
print("La nota minima es: ",notamin)

print("\n")
notamediana = statistics.median(notas)
print("La nota minima es: ",notamediana)
