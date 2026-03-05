


from db.database import conectar
import sqlite3


class MateriaRepositorio:
    def __init__(self, conexion):
        self.conexion = conexion

    def agregar(self, nombre, profesor_id):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("""
            INSERT INTO materia (nombre, profesor_id)
            VALUES (?, ?)
            """, (nombre, profesor_id))
            self.conexion.commit()
        
        except sqlite3.Error as e:
            raise Exception(f"Error al agregar materia.{e}")

    def listar(self):
        cursor = self.conexion.cursor()
        cursor.execute("""
        SELECT m.id, m.nombre, p.nombre, p.apellido
        FROM materia m
        JOIN profesor p ON m.profesor_id = p.id
        """)
        return cursor.fetchall()

    def eliminar(self, id):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM materia WHERE id = ?", (id,))
            self.conexion.commit()
        
        except sqlite3.Error as e:
            raise Exception(f"Error al eliminar materia. {e}")

