

from datetime import datetime
from database.conexion import conectar
from tabulate import tabulate

def notificar_alumnos_por_falta(profesor_id):
    conexion = conectar()
    cursor = conexion.cursor()

    # Buscar materias del profesor
    cursor.execute("SELECT id, nombre FROM materia WHERE profesor_id = ?", (profesor_id,))
    materias = cursor.fetchall()

    if not materias:
        print("El profesor no tiene materias asignadas.")
        conexion.close()
        return

    for materia in materias:
        materia_id, nombre_materia = materia
        print(f"\nAlumnos de la materia: {nombre_materia}")

        # Buscar alumnos inscriptos en esta materia
        cursor.execute("""
            SELECT alumno.nombre, alumno.apellido, alumno.correo
            FROM inscripcion
            JOIN alumno ON inscripcion.alumno_id = alumno.id
            WHERE inscripcion.materia_id = ?
        """, (materia_id,))
        alumnos = cursor.fetchall()

        if not alumnos:
            print("No hay alumnos inscriptos en esta materia.")
        else:
            for alumno in alumnos:
                nombre, apellido, correo = alumno
                print(f"- Notificando a {nombre} {apellido} ({correo})")

    conexion.close()


def registrar_falta():
    print("\n--- Registrar Falta de Profesor ---")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, apellido FROM profesor")
    profesores = cursor.fetchall()

    if not profesores:
        print("No hay profesores registrados.")
        conexion.close()
        return

    print("Profesores:")
    for p in profesores:
        print(f"{p[0]}: {p[1]} {p[2]}")

    profesor_id = input("ID del profesor ausente: ")

    motivo = input("Motivo (opcional): ")

    fecha_input = input("Ingrese la fecha (ejemplo: lunes - 28 - 2025): ").strip()
    if not fecha_input:
        fecha = datetime.today().strftime("%A - %d - %Y")
    else:
        fecha = fecha_input  # Para mejorar, podés validar formato aquí

    try:
        cursor.execute("""
            INSERT INTO falta (profesor_id, fecha, motivo)
            VALUES (?, ?, ?)
        """, (profesor_id, fecha, motivo))
        conexion.commit()
        print("Falta registrada correctamente.")
        notificar_alumnos_por_falta(profesor_id)
    except Exception as e:
        print("Error al registrar falta:", e)
    finally:
        conexion.close()


def listar_faltas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute('''
        SELECT f.id, f.fecha, f.motivo, p.nombre || ' ' || p.apellido AS profesor
        FROM falta f
        JOIN profesor p ON f.profesor_id = p.id
        ORDER BY f.fecha DESC
    ''')
    faltas = cursor.fetchall()
    conexion.close()

    if faltas:
        print("\n--- Listado de Faltas Registradas ---")
        print(tabulate(faltas, headers=["ID", "Fecha", "Motivo", "Profesor"], tablefmt="fancy_grid"))
    else:
        print("No hay faltas registradas.")