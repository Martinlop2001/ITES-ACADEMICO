



import sqlite3

class AlumnoRepositorio:
    def __init__(self, conexion):
        self.conexion = conexion

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

    def editar(self, id, dni, nombre, apellido, correo):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("""
            UPDATE alumno
            SET dni = ?, nombre = ?, apellido = ?, correo = ?
            WHERE id = ?
            """, (dni, nombre, apellido, correo, id))
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

    def obtener_por_dni(self, dni):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM alumno WHERE dni = ?", (dni,))
        return cursor.fetchone()
    
    def obtener_por_id(self, id):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM alumno WHERE id = ?", (id,))
        return cursor.fetchone()