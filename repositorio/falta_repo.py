


from db.database import conectar

def registrar_falta(materia_id, fecha, motivo):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO falta (materia_id, fecha, motivo)
        VALUES (?, ?, ?)
    """, (materia_id, fecha, motivo))

    conexion.commit()
    conexion.close()


def obtener_falta_por_materia_y_fecha(materia_id, fecha):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM falta 
        WHERE materia_id = ? AND fecha = ?
    """, (materia_id, fecha))

    resultado = cursor.fetchone()
    conexion.close()
    return resultado


def obtener_materia_por_id(materia_id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM materia WHERE id = ?", (materia_id,))
    resultado = cursor.fetchone()

    conexion.close()
    return resultado


def listar_faltas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT 
            falta.id,
            profesor.nombre || ' ' || profesor.apellido,
            materia.nombre,
            falta.fecha,
            falta.motivo
        FROM falta
        JOIN materia ON falta.materia_id = materia.id
        JOIN profesor ON materia.profesor_id = profesor.id
    """)

    faltas = cursor.fetchall()
    conexion.close()
    return faltas


def eliminar_faltas(id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM falta WHERE id = ?", (id,))

    conexion.commit()
    conexion.close()