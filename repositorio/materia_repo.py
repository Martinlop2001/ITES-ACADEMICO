


from db.database import conectar

def agregar_materia(nombre, profesor_id):
    if existe_materia(nombre):
        print("Ya existe una materia con ese nombre")
        return

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO materia (nombre, profesor_id)
    VALUES (?, ?)
    """, (nombre, profesor_id))

    conexion.commit()
    conexion.close()
    print("Materia agregada correctamente.")


def obtener_materia_por_nombre(nombre):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM materia WHERE nombre = ?", (nombre,))
    resultado = cursor.fetchone()
    
    conexion.close()
    return resultado



def listar_materias():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT materia.id, materia.nombre, profesor.nombre, profesor.apellido
    FROM materia
    LEFT JOIN profesor ON materia.profesor_id = profesor.id
    """)
    materias = cursor.fetchall()

    conexion.close()
    return materias


def editar_materia(id, nombre, profesor_id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    UPDATE materia
    SET nombre = ?, profesor_id = ?
    WHERE id = ?
    """, (nombre, profesor_id, id))


def eliminar_materia(id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM materia WHERE id = ?", (id,))
    
    conexion.commit()
    conexion.close()

#Validación de Materia

def existe_materia(nombre):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM materia WHERE nombre = ?", (nombre,))
    resultado = cursor.fetchone()

    conexion.close()
    return resultado is not None