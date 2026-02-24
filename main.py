


from db.database import crear_tablas
from servicios.falta_servicio import registrar_falta_servicio
from repositorio.falta_repo import listar_faltas, eliminar_faltas
from servicios.profesor_servicio import registrar_profesor_servicio
from repositorio.profesor_repo import listar_profesores, editar_profesor, eliminar_profesor
from servicios.alumno_servicio import registrar_alumno_servicio
from repositorio.alumno_repo import listar_alumnos, editar_alumno, eliminar_alumno
from servicios.materia_servicio import registrar_materia_servicio
from repositorio.materia_repo import listar_materias, editar_materia, eliminar_materia



def menu_principal():
    while True:
        print("============================")
        print("--- Ites Academico ---")
        print("1 - Gestion Profesores")
        print("2 - Gestion Alumnos")        
        print("3 - Gestion Materias")
        print("4 - Consultar Faltas")
        print("0 - Salir")
        print("============================")        

        opc = input("Seleccione una opcion: ")

        if opc == "1":
            menu_profesores()
        elif opc == "2":
            menu_alumnos()
        elif opc == "3":
            menu_materias()
        elif opc == "4":
            menu_faltas()
        elif opc == "0":
            break



def menu_profesores():
    while True:
        print("============================")
        print("--- Profesores ---")
        print("1 - Agregar Profesor")
        print("2 - Listar Profesor")
        print("3 - Editar Profesor")
        print("4 - Eliminar Profesor")
        print("0 - Volver")
        print("============================")

        opc = input("\nOpcion: ")

        if opc == "1":
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input ("Correo: ")
        
            exito, mensaje = registrar_profesor_servicio(dni, nombre, apellido, correo)
            print(mensaje)

        elif opc == "2":
            profesores = listar_profesores()
            for p in profesores:
                print(p)

        elif opc == "3":
            id = input("ID a editar: ")
            nombre = input("Nuevo Nombre: ")
            apellido = input("Nuevo Apellido: ")
            correo = input("Nuevo Correo: ")
            editar_profesor(id, nombre, apellido, correo)

        elif opc == "4":
            id = input("ID a eliminar: ")
            eliminar_profesor(id)
        
        elif opc == "0":
            break



def menu_alumnos():
    while True:
        print("============================")
        print("--- Menu Alumnos ---")
        print("1 - Agregar Alumno")
        print("2 - Listar Alumno")
        print("3 - Editar Alumno")
        print("4 - Eliminar Alumno")
        print("0 - Volver")
        print("============================")

        opc = input("\nOpcion: ")

        if opc == "1":
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input ("Correo: ")

            exito, mensaje = registrar_alumno_servicio(dni, nombre, apellido, correo)
            print(mensaje)


        elif opc == "2":
            alumnos = listar_alumnos()
            for a in alumnos:
                print(a)

        elif opc == "3":
            id = input("ID a editar: ")
            nombre = input("Nuevo Nombre: ")
            apellido = input("Nuevo Apellido: ")
            correo = input("Nuevo Correo: ")
            editar_alumno(id, nombre, apellido, correo)

        elif opc == "4":
            id = input("ID a eliminar: ")
            eliminar_alumno(id)
        
        elif opc == "0":
            break



def menu_materias():
    while True:
        print("============================")
        print("--- Menu Materias ---")
        print("1 - Agregar Materia")
        print("2 - Listar Materia")
        print("3 - Editar Materia")
        print("4 - Eliminar Materia")
        print("0 - Volver")
        print("============================")

        opc = input("\nOpcion: ")

        if opc == "1":
            nombre = input("Nombre Materia: ")
            profesor_id = input("Profesor_id: ")
        
            exito, mensaje = registrar_materia_servicio(nombre, profesor_id)
            print(mensaje)

        
        elif opc == "2":
            materias = listar_materias()
            for m in materias:
                print(m)

        elif opc == "3":
            id = input("ID de Materia a editar: ")
            nombre = input("Nombre Materia: ")
            profesor_id = input("Profesor_id: ")
            editar_materia(id, nombre, profesor_id)

        elif opc == "4":
            id = input("ID de Materia a eliminar: ")
            eliminar_materia(id)
        
        elif opc == "0":
            break




def menu_faltas():
    while True:
        print("============================")
        print("--- Menu Faltas ---")
        print("1 - Registrar Falta")
        print("2 - Listar Faltas")
        print("3 - Eliminar Falta")
        print("0 - Volver")
        print("============================")

        opc = input("\nOpcion: ")

        if opc == "1":
            materias = listar_materias()
            print("\nMaterias Disponibles: ")
            for m in materias:
                print(m)

            materia_id = input("ID de Materia: ")
            fecha = input("Fecha (YYYY/MM/DD): ")
            motivo = str(input("Motivo de la Falta: "))

            exito, mensaje = registrar_falta_servicio(materia_id, fecha, motivo)
            print(mensaje)

        elif opc == "2":
            faltas = listar_faltas()

            print("\n=========== LISTA DE FALTAS ===========")

            for f in faltas:
                print("----------------------------------------")
                print(f"ID: {f[0]}")
                print(f"Profesor: {f[1]}")
                print(f"Materia: {f[2]}")
                print(f"Fecha: {f[3]}")
                print(f"Motivo: {f[4]}")

            print("----------------------------------------")


        elif opc == "3":
            id = input("ID de Falta a Eliminar: ")
            eliminar_faltas(id)
        
        elif opc == "0":
            break





if __name__ == "__main__":
    crear_tablas()
    menu_principal()