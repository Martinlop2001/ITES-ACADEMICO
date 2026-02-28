


from db.database import conectar
import sqlite3


class FaltaRepositorio:
    def __init__(self, conexion):
        self.conexion = conectar()

    def registrar(self, profesor_id, materia_id, fecha, motivo):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("""
            INSERT INTO falta (profesor_id, materia_id, fecha, motivo)
            VALUES (?, ?, ?, ?)""", (profesor_id, materia_id, fecha, motivo))
            self.conexion.commit()

        except sqlite3.Error as e:
            raise Exception(f"Error al registrar falta. {e}")

    def listar(self):
        cursor = self.conexion.cursor()
        cursor.execute("""
        SELECT f.id,
                m.nombre AS materia,
                p.nombre || ' ' || p.apellido AS profesor,
                f.fecha,
                f.motivo,
            FROM falta f
            JOIN profesor p ON f.profesor_id = p.id,
            JOIN materia m ON f.materia_id = m.id
        """)
        return cursor.fetchall()

    def eliminar(self, id):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM falta WHERE id = ?", (id,))
            self.conexion.commit()

        except sqlite3.Error as e:
            raise Exception(f"Error al eliminar falta. {e}")