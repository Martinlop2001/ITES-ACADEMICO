



class Usuario:
    def __init__(self, username, password, rol, referencia_id=None):
        self.username = username
        self.password = password
        self.rol = rol
        self.referencia_id = referencia_id