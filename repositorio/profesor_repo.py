


from db.database import conectar
import sqlite3


class ProfesorRepositorio:
    def __init__(self, conexion):
        self.conexion = conectar()

    def agregar(self, dni, nombre, apellido, correo):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("""
                INSERT INTO profesor (dni, nombre, apellido, correo)
                VALUES (?, ?, ?, ?)
            """, (dni, nombre, apellido, correo))
            self.conexion.commit()

        except sqlite3.Error as e:
            raise Exception(f"Error al agregar profesor: {e}")
    
    def listar(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM profesor")
            return cursor.fetchall()
            
        except sqlite3.Error as e:
            raise Exception(f"Error al listar profesores: {e}")

    def editar(self, id, nombre, apellido, correo):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("""
            UPDATE profesor
            SET nombre = ?, apellido = ?, correo = ?
            WHERE id = ?
            """, (nombre, apellido, correo, id))
            self.conexion.commit()

        except sqlite3.Error as e:
            raise Exception(f"Error al editar profesor: {e}")

    def eliminar(self, id):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM profesor WHERE id = ?", (id,))
            self.conexion.commit()

        except sqlite3.Error as e:
            raise Exception(f"Error nal eliminar profesor: {e}")