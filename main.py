


from db.database import crear_tablas, conectar


from repositorio.profesor_repo import ProfesorRepositorio
from servicios.profesor_servicio import ProfesorServicio

from repositorio.alumno_repo import AlumnoRepositorio
from servicios.alumno_servicio import AlumnoServicio

from repositorio.materia_repo import MateriaRepositorio
from servicios.materia_servicio import MateriaServicio

from repositorio.falta_repo import FaltaRepositorio
from servicios.falta_servicio import FaltaServicio



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
        
            exito, mensaje = profesor_servicio.agregar(dni, nombre, apellido, correo)
            print(mensaje)

        elif opc == "2":
            profesores = profesor_servicio.listar()
            for p in profesores:
                print(p)

        elif opc == "3":
            id = input("ID a editar: ")
            nombre = input("Nuevo Nombre: ")
            apellido = input("Nuevo Apellido: ")
            correo = input("Nuevo Correo: ")
            profesor_servicio.editar(id, nombre, apellido, correo)

        elif opc == "4":
            id = input("ID a eliminar: ")
            profesor_servicio.eliminar(id)
        
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

            exito, mensaje = alumno_servicio.agregar(dni, nombre, apellido, correo)
            print(mensaje)


        elif opc == "2":
            alumnos = alumno_servicio.listar()
            for a in alumnos:
                print(a)

        elif opc == "3":
            id = input("ID a editar: ")
            nombre = input("Nuevo Nombre: ")
            apellido = input("Nuevo Apellido: ")
            correo = input("Nuevo Correo: ")
            alumno_servicio.editar(id, nombre, apellido, correo)

        elif opc == "4":
            id = input("ID a eliminar: ")
            alumno_servicio.eliminar(id)
        
        elif opc == "0":
            break



def menu_materias():
    while True:
        print("============================")
        print("--- Menu Materias ---")
        print("1 - Agregar Materia")
        print("2 - Listar Materia")
        print("3 - Eliminar Materia")
        print("0 - Volver")
        print("============================")

        opc = input("\nOpcion: ")

        if opc == "1":
            nombre = input("Nombre Materia: ")
            profesor_id = input("Profesor_id: ")
        
            exito, mensaje = materia_servicio.agregar_materia(nombre, profesor_id)
            print(mensaje)

        
        elif opc == "2":
            materias = materia_servicio.listar_materias()
            for m in materias:
                print(m)

        elif opc == "3":
            id = input("ID de Materia a eliminar: ")
            materia_servicio.eliminar_materia(id)
        
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
            materias = materia_servicio.listar_materias()
            print("\nMaterias Disponibles: ")
            for m in materias:
                print(m)

            profesor_id = int(input("ID del Profesor: "))
            materia_id = int(input("ID de Materia: "))
            fecha = input("Fecha (YYYY/MM/DD): ")
            motivo = input("Motivo de la Falta: ")

            exito, mensaje = falta_servicio.registrar_falta(
                profesor_id,
                materia_id,
                fecha,
                motivo
            )
            print(mensaje)

        elif opc == "2":
            faltas = falta_servicio.listar_falta()

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
            falta_servicio.eliminar_falta(id)
        
        elif opc == "0":
            break





if __name__ == "__main__":
    
    crear_tablas()
    conexion = conectar()
    conexion.execute("PRAGMA foreign_keys = ON")

    profesor_repo = ProfesorRepositorio(conexion)
    alumno_repo = AlumnoRepositorio(conexion)
    materia_repo = MateriaRepositorio(conexion)
    falta_repo = FaltaRepositorio(conexion)

    profesor_servicio = ProfesorServicio(profesor_repo)
    alumno_servicio = AlumnoServicio(alumno_repo)
    falta_servicio = FaltaServicio(falta_repo)
    materia_servicio = MateriaServicio(materia_repo)

    menu_principal()
    conexion.close()