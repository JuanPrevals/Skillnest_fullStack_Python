# Importamos las clases del proyecto
from estudiante import Estudiante
from calificacion import Calificacion


# =====================================
# MENÚ PRINCIPAL

while True:

    print("\n")
    print("===================================")
    print("     SISTEMA ESCOLAR 3FN")
    print("===================================")

    print("1. Listar estudiantes")
    print("2. Buscar estudiante")
    print("3. Agregar estudiante")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("6. Listar asignaturas")
    print("7. Registrar calificación")
    print("8. Ver calificaciones")
    print("9. Ver notas de un estudiante")
    print("10. Buscar notas por rango")
    print("11. Ver promedios")
    print("12. Salir")

    opcion = input(
        "\nSeleccione una opción: "
    )
    # LISTAR ESTUDIANTES
    if opcion == "1":
        Estudiante.listar()
    # BUSCAR ESTUDIANTE
    elif opcion == "2":
        Estudiante.buscar()
    # AGREGAR ESTUDIANTE
    elif opcion == "3":
        print("\n===== NUEVO ESTUDIANTE =====")
        nombre = input("Nombre del estudiante: ")
        curso = input("Curso: ")
        # Creamos un objeto
        estudiante = Estudiante(nombre,curso)
        # Utilizamos el método del objeto
        estudiante.guardar()
    # ACTUALIZAR ESTUDIANTE
    elif opcion == "4":
        Estudiante.actualizar()
    # ELIMINAR ESTUDIANTE
    elif opcion == "5":
        Estudiante.eliminar()
    # LISTAR ASIGNATURAS
    elif opcion == "6":
        Calificacion.listar_asignaturas()
    # REGISTRAR CALIFICACIÓN
    elif opcion == "7":
        print("\n===== REGISTRAR CALIFICACIÓN =====")
        print("\nESTUDIANTES DISPONIBLES")
        Estudiante.listar()
        id_estudiante = int(input("\nIngrese ID del estudiante: "))
        print("\nASIGNATURAS DISPONIBLES")
        Calificacion.listar_asignaturas()
        id_asignatura = int(input("\nIngrese ID de la asignatura: "))
        nota = float(input("Ingrese la nota: "))
        fecha = input("Fecha (AAAA-MM-DD): ")
        # Creamos el objeto Calificacion
        calificacion = Calificacion(id_estudiante,id_asignatura,nota,fecha)
        # Guardamos utilizando el método
        # del objeto
        calificacion.guardar()
    # VER CALIFICACIONES
    elif opcion == "8":
        Calificacion.ver_calificaciones()
    # VER NOTAS DE UN ESTUDIANTE
    elif opcion == "9":
        print("\nESTUDIANTES DISPONIBLES")
        Estudiante.listar()
        Calificacion.ver_notas_estudiante()
    # BUSCAR POR RANGO
    elif opcion == "10":
        Calificacion.buscar_por_rango()
    # VER PROMEDIOS
    elif opcion == "11":
        Calificacion.ver_promedios()
    # SALIR
    elif opcion == "12":
        print("\nPrograma finalizado.")
        break
    else:
        print(
            "\nOpción inválida."
        )