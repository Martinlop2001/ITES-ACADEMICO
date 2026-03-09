



class MateriaRepositorio:
    def __init__(self, conexion):
        self.conexion = conexion

    def agregar(self, nombre, profesor_id):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("""
            INSERT INTO materia (nombre, profesor_id)
            VALUES (%s, %s)
            """, (nombre, profesor_id))
            self.conexion.commit()
        
        except Exception as e:
            raise Exception(f"Error al agregar materia.{e}")

    def listar(self):
        cursor = self.conexion.cursor()
        cursor.execute("""
        SELECT m.id, m.nombre, p.nombre, p.apellido
        FROM materia m
        JOIN profesor p ON m.profesor_id = p.id
        """)
        return cursor.fetchall()

    def listar_por_profesor(self, profesor_id):
        cursor = self.conexion.cursor()
        cursor.execute("""
        SELECT id, nombre FROM materia WHERE profesor_id = %s
        """, (profesor_id,))
        return cursor.fetchall()

    def obtener_por_id(self, id):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM materia WHERE id = %s", (id,))
        return cursor.fetchone()

    def eliminar(self, id):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM materia WHERE id = %s", (id,))
            self.conexion.commit()
        
        except Exception as e:
            raise Exception(f"Error al eliminar materia. {e}")

