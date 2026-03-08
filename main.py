



from db.database import crear_tablas, conectar

from repositorio.profesor_repo import ProfesorRepositorio
from servicios.profesor_servicio import ProfesorServicio

from repositorio.alumno_repo import AlumnoRepositorio
from servicios.alumno_servicio import AlumnoServicio

from repositorio.materia_repo import MateriaRepositorio
from servicios.materia_servicio import MateriaServicio

from repositorio.falta_repo import FaltaRepositorio
from servicios.falta_servicio import FaltaServicio

from repositorio.usuario_repo import UsuarioRepositorio
from servicios.usuario_servicio import UsuarioServicio


# ================= LOGIN =================

def iniciar_sesion(usuario_servicio):

    username = input("Usuario: ")
    password = input("Contraseña: ")

    success, mensaje, usuario = usuario_servicio.login(username, password)

    print(mensaje)

    if success:
        rol = usuario[3]

        if rol == "admin":
            menu_admin()

        elif rol == "profesor":
            menu_profesor(usuario)

        elif rol == "alumno":
            menu_alumno(usuario)


# ================= MENUS POR ROL =================

def registrar_falta(profesor_id):

    print("\n--- REGISTRAR FALTA ---")

    print("\nAlumnos disponibles:")
    alumnos = alumno_servicio.listar()
    for a in alumnos:
        print(f"ID: {a[0]} - {a[2]} {a[3]}")

    print("\nMaterias disponibles:")
    materias = materia_servicio.listar_materias()
    for m in materias:
        print(f"ID: {m[0]} - {m[1]}")

    alumno_id = input("ID del Alumno: ")
    materia_id = input("ID de la Materia: ")
    fecha = input("Fecha (YYYY-MM-DD): ")
    motivo = input("Motivo: ")

    exito, mensaje = falta_servicio.registrar_falta(
        alumno_id,
        profesor_id,
        materia_id,
        fecha,
        motivo
    )

    print(mensaje)


def menu_profesor(usuario):

    profesor_id = usuario[4]

    while True:

        print("\n=== MENU PROFESOR ===")
        print("1 - Registrar falta")
        print("2 - Ver faltas registradas")
        print("0 - Cerrar sesión")

        opcion = input("Opcion: ")

        if opcion == "1":
            registrar_falta(profesor_id)

        elif opcion == "2":

            faltas = falta_servicio.listar_falta()

            for f in faltas:
                print(f)

        elif opcion == "0":
            break


def menu_alumno(usuario):
    alumno_id = usuario[4]

    while True:
        print("\n=== MENU ALUMNO ===")
        print("1 - Ver mis faltas")
        print("0 - Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            faltas = falta_servicio.listar_falta(alumno_id)

            if not faltas:
                print("No tenés faltas registradas.")
            else:
                print("\nID | Materia | Fecha | Motivo")
                print("--------------------------------")

                for f in faltas:
                    print(f)

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")


# ======================== MENU DE INICIO =========================

def menu_inicio():
    while True:
        print("============================")
        print("1 - Iniciar Sesión")
        print("2 - Registrarse como Alumno")
        print("0 - Salir")
        print("============================")

        opc = input("Opcion: ")

        if opc == "1":
            iniciar_sesion(usuario_servicio)

        elif opc == "2":
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            username = input("Username: ")
            password = input("Password: ")

            exito, mensaje = usuario_servicio.registrar_alumno(dni, nombre, apellido, correo, username, password)
            print(mensaje)

        elif opc == "0":
            break


# ================= MENU PRINCIPAL (ADMIN) =================

def menu_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1 - Gestionar profesores")
        print("2 - Gestionar alumnos")
        print("3 - Gestionar materias")
        print("4 - Gestionar faltas")
        print("5 - Crear usuario profesor")
        print("0 - Cerrar sesión")

        opc = input("Seleccione una opcion: ")

        if opc == "1":
            menu_profesores()
        elif opc == "2":
            menu_alumnos()
        elif opc == "3":
            menu_materias()
        elif opc == "4":
            menu_faltas()

        elif opc == "5":

            profesor_servicio.listar()

            profesor_id = input("ID del profesor: ")
            username = input("Username: ")
            password = input("Password: ")

            exito, mensaje = usuario_servicio.registrar_profesor(
                username,
                password,
                profesor_id
            )

            print(mensaje)

        elif opc == "0":
            break


# ================= SUBMENUS PARA ADMIN =================

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
            correo = input("Correo: ")

            exito, mensaje = profesor_servicio.agregar(dni, nombre, apellido, correo)
            print(mensaje)

        elif opc == "2":
            profesores = profesor_servicio.listar()
            for p in profesores:
                print(p)

        elif opc == "3":
            id = input("ID a editar: ")
            profesor = profesor_servicio.obtener_por_id(id)

            if not profesor:
                print("No existe un profesor con ese ID.")
                continue

            dni_actual = profesor[1]
            nombre_actual = profesor[2]
            apellido_actual = profesor[3]
            correo_actual = profesor[4]

            dni = input(f"Nuevo DNI ({dni_actual}): ") or dni_actual
            nombre = input(f"Nuevo nombre ({nombre_actual}): ") or nombre_actual
            apellido = input(f"Nuevo apellido ({apellido_actual}): ") or apellido_actual
            correo = input(f"Nuevo correo ({correo_actual}): ") or correo_actual

            exito, mensaje = profesor_servicio.editar(id, dni, nombre, apellido, correo)
            print(mensaje)

        elif opc == "4":
            id = input("ID a eliminar: ")
            profesor = profesor_servicio.obtener_por_id(id)

            if not profesor:
                print("No existe un profesor con ese ID.")
                continue

            confirmar = input(f"Esta accion eliminara al profesor {profesor[2]} {profesor[3]} y todas sus materias y faltas asociadas. ¿Seguro que deseas continuar? (s/n): ").lower()
            if confirmar != "s":
                print("Operacion cancelada.")
                continue

            exito, mensaje = profesor_servicio.eliminar(id)
            print(mensaje)

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
            correo = input("Correo: ")

            exito, mensaje = alumno_servicio.agregar(dni, nombre, apellido, correo)
            print(mensaje)

        elif opc == "2":
            alumnos = alumno_servicio.listar()
            for a in alumnos:
                print(a)

        elif opc == "3":
            id = input("ID a editar: ")
            alumno = alumno_servicio.obtener_por_id(id)

            if not alumno:
                print("No existe un alumno con ese ID.")
                continue

            dni_actual = alumno[1]
            nombre_actual = alumno[2]
            apellido_actual = alumno[3]
            correo_actual = alumno[4]

            dni = input(f"Nuevo DNI ({dni_actual}): ") or dni_actual
            nombre = input(f"Nuevo nombre ({nombre_actual}): ") or nombre_actual
            apellido = input(f"Nuevo apellido ({apellido_actual}): ") or apellido_actual
            correo = input(f"Nuevo correo ({correo_actual}): ") or correo_actual

            exito, mensaje = alumno_servicio.editar(id, dni, nombre, apellido, correo)
            print(mensaje)

        elif opc == "4":
            id = input("ID a eliminar: ")
            alumno = alumno_servicio.obtener_por_id(id)

            if not alumno:
                print("No existe un alumno con ese ID.")
                continue

            confirmar = input(f"Esta accion eliminara al alumno {alumno[2]} {alumno[3]} y todas sus faltas asociadas. ¿Seguro que deseas continuar? (s/n): ").lower()
            if confirmar != "s":
                print("Operacion cancelada.")
                continue

            exito, mensaje = alumno_servicio.eliminar(id)
            print(mensaje)

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
            materias = materia_servicio.listar_materias()
            materia_encontrada = next((m for m in materias if str(m[0]) == id), None)

            if not materia_encontrada:
                print("No existe una materia con ese ID.")
                continue

            confirmar = input(f"Esta accion eliminara la materia {materia_encontrada[1]} y todas sus faltas asociadas. ¿Seguro que deseas continuar? (s/n): ").lower()
            if confirmar != 's':
                print("Operacion cancelada.")
                continue

            exito, mensaje = materia_servicio.eliminar_materia(id)
            print(mensaje)

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
            print("\n--- ALUMNOS DISPONIBLES ---")
            alumnos = alumno_servicio.listar()
            for a in alumnos:
                print(f"ID: {a[0]} - {a[2]} {a[3]}")
            print("\n--- PROFESORES DISPONIBLES ---")
            profesores = profesor_servicio.listar()
            for p in profesores:
                print(f"ID: {p[0]} - {p[2]} {p[3]}")
            print("\n--- MATERIAS DISPONIBLES ---")
            materias = materia_servicio.listar_materias()
            for m in materias:
                print(f"ID: {m[0]} - {m[1]}")

            alumno_id = input("ID del Alumno: ")
            profesor_id = input("ID del Profesor: ")
            materia_id = input("ID de Materia: ")
            fecha = input("Fecha (YYYY/MM/DD): ")
            motivo = input("Motivo de la Falta: ")

            exito, mensaje = falta_servicio.registrar_falta(
                alumno_id,
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
            confirmar = input(f"Esta accion eliminara la falta con ID {id}. ¿Seguro que deseas continuar? (s/n): ").lower()
            if confirmar != "s":
                print("Operacion cancelada.")
                continue

            exito, mensaje = falta_servicio.eliminar_falta(id)
            print(mensaje)

        elif opc == "0":
            break


# ================= EJECUCION =================

if __name__ == "__main__":

    crear_tablas()
    conexion = conectar()
    conexion.execute("PRAGMA foreign_keys = ON")

    profesor_repo = ProfesorRepositorio(conexion)
    alumno_repo = AlumnoRepositorio(conexion)
    materia_repo = MateriaRepositorio(conexion)
    falta_repo = FaltaRepositorio(conexion)
    usuario_repo = UsuarioRepositorio(conexion)

    profesor_servicio = ProfesorServicio(profesor_repo)
    alumno_servicio = AlumnoServicio(alumno_repo)
    materia_servicio = MateriaServicio(materia_repo)
    falta_servicio = FaltaServicio(falta_repo)
    usuario_servicio = UsuarioServicio(usuario_repo, alumno_servicio)

    usuario_servicio.crear_admin_inicial()

    menu_inicio()

    conexion.close()
