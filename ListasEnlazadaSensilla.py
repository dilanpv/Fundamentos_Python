# class NodoAmigo:
#     def __init__(self, dato): #Constructor
#         self.dato = dato
#         self.siguiente = None

# class ListaEnlazada:
#     def __init__(self):
#         self.head = None
#     #Metodo para insertar un nuevo nodo al inicio de la lista
#     def insertar_al_principio(self, dato):
#         nuevo_nodo = NodoAmigo(dato)
#         nuevo_nodo.siguiente = self.head
#         self.head = nuevo_nodo
        
#     def recorrer(self):
#         actual = self.head
#         while actual is not None:
#             print(actual.dato, end="-> ")
#             actual = actual.siguiente
#         print("NULL")

# #Llamamos al constructor
# lista = ListaEnlazada()

# #Se insertan datos a los nodos
# lista.insertar_al_principio("A")
# lista.insertar_al_principio("E")
# lista.insertar_al_principio("I")
# lista.insertar_al_principio("O")
# lista.insertar_al_principio("U")

# #Se recorre cada nodo
# lista.recorrer()


# class NodoAmigo:
#     def __init__(self, dato):  # Constructor
#         self.dato = dato
#         self.siguiente = None
#         self.prev = None  # Puntero al nodo anterior

# class ListaDoblementeEnlazada:
#     def __init__(self):
#         self.cabeza = None
#     # Método para insertar un nuevo nodo al inicio de la lista
#     def insertar_al_principio(self, dato):
#         nuevo_nodo = NodoAmigo(dato)
#         nuevo_nodo.siguiente = self.cabeza
#         if self.cabeza is not None:
#             self.cabeza.prev = nuevo_nodo  # Apunta hacia atrás al nuevo nodo
#         self.cabeza = nuevo_nodo

#     def recorrer(self):
#         actual = self.cabeza
#         while actual is not None:
#             print(actual.dato, end=" <-> ")
#             actual = actual.siguiente
#         print("NULL")

# # Llamamos al constructor
# lista = ListaDoblementeEnlazada()

# # Se insertan datos a los nodos
# lista.insertar_al_principio("A")
# lista.insertar_al_principio("E")
# lista.insertar_al_principio("I")
# lista.insertar_al_principio("O")
# lista.insertar_al_principio("U")

# # Se recorre cada nodo
# lista.recorrer()

#   2 ejercicios de listas sencillas aplicado a la realidad, 5 de listas enlazdas, 5 de colas, 5 pilas.

# --- LISTAS SIMPLES ---
# 1. Registro de compras
compras = []
for i in range(3):
    item = input("Producto comprado: ")
    compras.append(item)
print("Tu lista de compras:", compras)

# 2. Buscar canción en una lista
canciones = ["Perfect", "Flowers", "Houdini", "TQG"]
buscar = input("Canción que buscas: ")
if buscar in canciones:
    print("Está en tu lista de reproducción.")
else:
    print("No la tienes guardada.")

# --- COLAS ---
# 1.Fila en un banco
cola = []
cola.append("Monica")
cola.append("Luis")
cola.append("Marta")
print("Primero en la fila:", cola[0])
cola.pop(0)
print("Ahora sigue:", cola[0])

# 2. Cola de atención en un restaurante
cola = []
for i in range(3):
    nombre = input("Nombre cliente: ")
    cola.append(nombre)

while cola:
    print("Atendiendo a:", cola.pop(0))
