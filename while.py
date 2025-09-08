asignaturas = []
opcion = 0
while opcion != 4:
    print("\n--- SISTEMA ACADÉMICO ---")
    print("1. Ver asignaturas inscritas")
    print("2. Agregar una asignatura")
    print("3. Eliminar una asignatura")
    print("4. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    # Opción 1: ver asignaturas
    if opcion == 1:
        if len(asignaturas) == 0:
            print("No tienes asignaturas inscritas.")
        else:
            print("Asignaturas inscritas:")
            for materia in asignaturas:
                print("-", materia)
    
    # Opción 2: agregar asignatura
    elif opcion == 2:
        if len(asignaturas) >= 6:
            print("No puedes inscribir más de 6 asignaturas.")
        else:
            nueva = input("Ingrese el nombre de la asignatura: ")
            if nueva in asignaturas:
                print("Esa asignatura ya está inscrita.")
            else:
                asignaturas.append(nueva)
                print("Asignatura agregada con éxito.")
    
    # Opción 3: eliminar asignatura
    elif opcion == 3:
        eliminar = input("Ingrese el nombre de la asignatura a eliminar: ")
        if eliminar in asignaturas:
            asignaturas.remove(eliminar)
            print("Asignatura eliminada correctamente.")
        else:
            print("No tienes inscrita esa asignatura.")
    
    # Opción 4: salir
    elif opcion == 4:
        print("Saliendo del sistema... ¡Hasta luego!")
    
    # Cualquier otro número
    else:
        print("Opción no válida, intente de nuevo.")