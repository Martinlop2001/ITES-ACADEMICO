


from db.database import conectar

def agregar_profesor(dni, nombre, apellido, correo):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO profesor (dni, nombre, apellido, correo)
        VALUES (?, ?, ?, ?)
    """, (dni, nombre, apellido, correo))

    conexion.commit()
    conexion.close()


def obtener_profesor_por_dni(dni):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM profesor WHERE dni = ?", (dni,))
    resultado = cursor.fetchone()

    conexion.close()
    return resultado


def listar_profesores():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM profesor")
    profesores = cursor.fetchall()

    conexion.close()
    return profesores


def editar_profesor(id, nombre, apellido, correo):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE profesor
        SET nombre = ?, apellido = ?, correo = ?
        WHERE id = ?
    """, (nombre, apellido, correo, id))

    conexion.commit()
    conexion.close()


def eliminar_profesor(id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM profesor WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()