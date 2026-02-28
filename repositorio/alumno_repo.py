


from db.database import conectar
import sqlite3


class AlumnoRepositorio:
    def __init__(self, conexion):
        self.conexion = conectar()

    def agregar(self, dni, nombre, apellido, correo):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("""
            INSERT INTO alumno (dni, nombre, apellido, correo)
            VALUES (?, ?, ?, ?)
            """, (dni, nombre, apellido, correo))
            self.conexion.commit()

        except sqlite3.Error as e:
            raise Exception(f"Error al agregar alumno. {e}")

    def listar(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM alumno")
            return cursor.fetchall()

        except sqlite3.Error as e:
            raise Exception(f"Error al listar alumno. {e}")

    def editar(self, id, nombre, apellido, correo):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("""
            UPDATE alumno
            SET nombre = ?, apellido = ?, correo = ?
            WHERE id = ?
            """, (nombre, apellido, correo, id))
            self.conexion.commit()

        except sqlite3.Error as e:
            raise Exception(f"Error al editar alumno. {e}")

    def eliminar(self, id):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM alumno WHERE id = ?", (id,))
            self.conexion.commit()

        except sqlite3.Error as e:
            raise Exception(f"Error al eliminar alumno. {e}")