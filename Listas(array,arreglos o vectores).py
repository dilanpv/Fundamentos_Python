# lista = [10,21,2.2,11]

# for run in lista:
#     print(run)
    
# numeros = []

# numeros.append(11)
# numeros.append(114)
# numeros.append(1112)
# numeros.append(121)
# numeros.append(1)

# print(numeros)

# numeros = []

# #se une la lista antetior con una nueva
# numeros = numeros + [2,3,5]
# print(numeros)

#Remover un elemento de una lista en base a su indice.
# palabras = ["hola","que","más"]
# palabras.pop(1)
# print(palabras)

#el remove() elimina por coincidencia al primero lo mata.

biblioteca = []
notas = []
opc= 0
promedio = 0
while opc != 6:
    print("1.Ingresar Libros.")
    print("2.Eliminar un libro indicando su indice.(pop)")
    print("3.Eliminar un libro en base a su coincidencia(remove)")
    print("4. Ver la lista de libros.")
    print("5. Ingresar las notas.")
    print("6. Sacar el promedio de notas.")
    print("7.Salir")
    opc = int(input("Digite la opcion:"))
    if opc == 1:
        for i in range(0,11):
            libros = input("Ingrese el nombre del libro:")
            biblioteca.append(libros)
    elif opc == 2:
        eliminar = int(input("Digite el indice:"))
        biblioteca.pop(eliminar)
        
    elif opc == 3:
        delete = input("Ingrese el nombre del libro a eliminar:")
        biblioteca.remove(delete)
        
    elif opc == 4:
        for run in biblioteca:
            print(run)
    elif opc == 5:
        for i in range(5):
            nota = float(input(f"Digite la nota: {i+1}:"))
            notas.append(nota)
    elif opc == 6:
        for i  in range(len(notas)):
            print(f"estudiante  {i+1}: {notas[i]}") 
            promedio = sum(notas)/len(notas)
            print("El promedio es igual a: ",promedio)
        notamax = max(notas)
        print("La nota mas alta es: ",notamax)
        print("\n")
        notamin = min(notas)
        print("La nota minima es: ",notamin)
    elif opc == 7:
        print("Gracias")
        break
    else:
        print("Se equivoco de opc")