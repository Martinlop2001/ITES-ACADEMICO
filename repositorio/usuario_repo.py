


class UsuarioRepositorio:
    def __init__(self, conexion):
        self.conexion = conexion

    def agregar(self, username, password_hash, rol, referencia_id):
        cursor = self.conexion.cursor()
        cursor.execute("""
        INSERT INTO usuario (username, password, rol, referencia_id)
        VALUES (?, ?, ?, ?)
        """, (username, password_hash, rol, referencia_id))
        self.conexion.commit()

    def obtener_por_username(self, username):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM usuario WHERE username = ?", (username,))
        return cursor.fetchone()

    def listar(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM usuario")
        return cursor.fetchall()