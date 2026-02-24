


from db.database import conectar

def agregar_alumno(dni, nombre, apellido, correo):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO alumno (dni, nombre, apellido, correo)
    VALUES (?, ?, ?, ?)
""", (dni, nombre, apellido, correo))

    conexion.commit()
    conexion.close()


def obtener_alumno_por_dni(dni):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM alumno WHERE dni = ?", (dni,))
    resultado = cursor.fetchone()

    conexion.close()
    return resultado


def listar_alumnos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM alumnos")
    alumnos = cursor.fetchall()

    conexion.close()
    return alumnos


def editar_alumno(id, nombre, apellido, correo):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    UPDATE alumno
    SET nombre = ?, apellido = ?, correo = ?
    WHERE id = ?
    """, (nombre, apellido, correo, id))

    conexion.commit()
    conexion.close()


def eliminar_alumno(id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM alumno WHERE id = ?", (id,))

    conexion.commit()
    conexion.close()