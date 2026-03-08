



import sqlite3

class FaltaRepositorio:
    def __init__(self, conexion):
        self.conexion = conexion

    def registrar(self, alumno_id, profesor_id, materia_id, fecha, motivo):

        cursor = self.conexion.cursor()

        cursor.execute("""
            INSERT INTO falta (alumno_id, profesor_id, materia_id, fecha, motivo)
            VALUES (?, ?, ?, ?, ?)
        """, (alumno_id, profesor_id, materia_id, fecha, motivo))

        self.conexion.commit()

    def listar(self):
        cursor = self.conexion.cursor()
        cursor.execute("""
        SELECT
            f.id,
            p.nombre || ' ' || p.apellido AS profesor,
            m.nombre AS materia,
            f.fecha,
            f.motivo
        FROM falta f
        JOIN profesor p ON f.profesor_id = p.id
        JOIN materia m ON f.materia_id = m.id
        """)
        return cursor.fetchall()

    def listar_por_alumno(self, alumno_id):

        cursor = self.conexion.cursor()

        cursor.execute("""
            SELECT f.id, m.nombre, f.fecha, f.motivo
            FROM falta f
            JOIN materia m ON f.materia_id = m.id
            WHERE f.alumno_id = ?
        """, (alumno_id,))

        return cursor.fetchall()

    def eliminar(self, id):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM falta WHERE id = ?", (id,))
            self.conexion.commit()

        except sqlite3.Error as e:
            raise Exception(f"Error al eliminar falta. {e}")