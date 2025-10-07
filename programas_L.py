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

# 3. Eliminar una tarea completada
tareas = ["Estudiar", "Hacer ejercicio", "Limpiar"]
print("Tareas actuales:", tareas)
hecha = input("¿Qué tarea completaste?: ")
if hecha in tareas:
    tareas.remove(hecha)
print("Pendientes:", tareas)

# --- LISTAS DOBLEMENTE ENLAZADAS ---

#  Agenda de contactos
nombres = ["Ana", "Luis", "Marta"]
telefonos = ["111", "222", "333"]
for i in range(len(nombres)):
    print(nombres[i], "-", telefonos[i])

#  Ver contactos en orden inverso
nombres = ["Ana", "Luis", "Marta"]
telefonos = ["111", "222", "333"]
for i in range(len(nombres)-1, -1, -1):
    print(nombres[i], "-", telefonos[i])

#  Unir dos agendas
agenda1 = ["Ana", "Luis"]
agenda2 = ["Marta", "Pedro"]
agenda_total = agenda1 + agenda2
print("Agenda total:", agenda_total)

# --- PILA ---

# Historial de navegación
pila = []
pila.append("Inicio")
pila.append("Tienda")
pila.append("Carrito")
print("Actual:", pila[-1])
pila.pop()
print("Volviste a:", pila[-1])

# --- COLAS ---

# 1. Fila en un banco
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
