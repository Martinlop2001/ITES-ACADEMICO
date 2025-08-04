

from servicios import inscripciones
from servicios import gestion_profesores, gestion_alumnos
from servicios import gestion_materias
from servicios import faltas

def mostrar_menu():
    while True:
        print("\n--- Ites-Academico ---")
        print("1. Gestión de Profesores")
        print("2. Gestión de Alumnos")
        print("3. Gestión de Materias")
        print("4. Registrar Falta de Profesor")
        print("5. Consultar Faltas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_profesores()
        elif opcion == "2":
            menu_alumnos()
        elif opcion == "3":
            menu_materias()
        elif opcion == "4":
            faltas.registrar_falta()
        elif opcion == "5":
            faltas.listar_faltas()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_profesores():
    while True:
        print("\n--- Gestión de Profesores ---")
        print("1. Agregar profesor")
        print("2. Listar profesores")
        print("3. Editar profesor")
        print("4. Eliminar profesor")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestion_profesores.agregar_profesor()
        elif opcion == "2":
            gestion_profesores.listar_profesores()
        elif opcion == "3":
            gestion_profesores.editar_profesor()
        elif opcion == "4":
            gestion_profesores.eliminar_profesor()
        elif opcion == "0":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")

def menu_alumnos():
    while True:
        print("\n--- Gestión de Alumnos ---")
        print("1. Agregar alumno")
        print("2. Listar alumnos")
        print("3. Editar alumno")
        print("4. Eliminar alumno")
        print("5. Inscribir alumno a una materia")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestion_alumnos.agregar_alumno()
        elif opcion == "2":
            gestion_alumnos.listar_alumnos()
        elif opcion == "3":
            gestion_alumnos.editar_alumno()
        elif opcion == "4":
            gestion_alumnos.eliminar_alumno()
        elif opcion == "5":
            inscripciones.inscribir_alumno()
        elif opcion == "0":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")

def menu_materias():
    while True:
        print("\n--- Gestión de Materias ---")
        print("1. Agregar materia")
        print("2. Listar materias")
        print("3. Editar materia")
        print("4. Eliminar materia")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestion_materias.agregar_materia()
        elif opcion == "2":
            gestion_materias.listar_materias()
        elif opcion == "3":
            gestion_materias.editar_materia()
        elif opcion == "4":
            gestion_materias.eliminar_materia()
        elif opcion == "0":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")