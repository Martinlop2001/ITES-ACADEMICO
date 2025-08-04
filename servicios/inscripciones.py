

from database.conexion import conectar

def inscribir_alumno():
    conexion = conectar()
    cursor = conexion.cursor()

    # Mostrar alumnos
    cursor.execute("SELECT id, nombre, apellido FROM alumno")
    alumnos = cursor.fetchall()
    if not alumnos:
        print("No hay alumnos registrados.")
        return
    print("\n--- Alumnos disponibles ---")
    for a in alumnos:
        print(f"{a[0]}. {a[1]} {a[2]}")
    alumno_id = input("Ingrese el ID del alumno que desea inscribir: ")

    # Mostrar materias
    cursor.execute("""
        SELECT m.id, m.nombre, p.nombre || ' ' || p.apellido AS profesor
        FROM materia m
        JOIN profesor p ON m.profesor_id = p.id
    """)
    materias = cursor.fetchall()
    if not materias:
        print("No hay materias registradas.")
        return
    print("\n--- Materias disponibles ---")
    for m in materias:
        print(f"{m[0]}. {m[1]} (Profesor: {m[2]})")
    materia_id = input("Ingrese el ID de la materia: ")

    # Registrar la inscripción
    cursor.execute("INSERT INTO inscripcion (alumno_id, materia_id) VALUES (?, ?)", (alumno_id, materia_id))
    conexion.commit()
    conexion.close()

    print("Inscripción realizada con éxito.")