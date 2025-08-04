

from database.conexion import conectar

def notificar_alumnos_por_falta(profesor_id):
    conexion = conectar()
    cursor = conexion.cursor()

    # Obtener materias del profesor
    cursor.execute("SELECT id, nombre FROM materia WHERE profesor_id = ?", (profesor_id,))
    materias = cursor.fetchall()

    if not materias:
        print("El profesor no tiene materias asignadas.")
        conexion.close()
        return

    print("\n🔔 Notificando a los alumnos por la falta del profesor...")

    for materia in materias:
        materia_id, nombre_materia = materia

        # Buscar alumnos inscriptos en esta materia
        cursor.execute("""
            SELECT alumno.nombre, alumno.apellido, alumno.correo
            FROM inscripcion
            JOIN alumno ON inscripcion.alumno_id = alumno.id
            WHERE inscripcion.materia_id = ?
        """, (materia_id,))
        alumnos = cursor.fetchall()

        if not alumnos:
            print(f"No hay alumnos inscriptos en la materia: {nombre_materia}")
            continue

        print(f"\nMateria: {nombre_materia}")
        for alumno in alumnos:
            nombre, apellido, correo = alumno
            print(f"Se notificó a {nombre} {apellido} ({correo})")

    conexion.close()