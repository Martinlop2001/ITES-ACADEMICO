



import hashlib

class UsuarioServicio:
    def __init__(self, usuario_repo, alumno_servicio):
        self.usuario_repo = usuario_repo
        self.alumno_servicio = alumno_servicio

    def encriptar_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def registrar_alumno(self, dni, nombre, apellido, correo, username, password):
        try:
            exito, mensaje = self.alumno_servicio.agregar(dni, nombre, apellido, correo)

            if not exito:
                return False, mensaje

            alumno = self.alumno_servicio.obtener_por_dni(dni)
            alumno_id = alumno[0]

            password_hash = self.encriptar_password(password)

            self.usuario_repo.agregar(username, password_hash, "alumno", alumno_id)

            return True, "Alumno registrado correctamente."

        except Exception as e:
            return False, f"Error en registro: {e}"

    def login(self, username, password):
        try:
            usuario = self.usuario_repo.obtener_por_username(username)

            if not usuario:
                return False, "Usuario no encontrado.", None

            password_hash = self.encriptar_password(password)

            if usuario[2] != password_hash:
                return False, "Contraseña incorrecta.", None

            return True, "Login correcto.", usuario

        except Exception as e:
            return False, f"Error en login: {e}", None


    def crear_admin_inicial(self):
        try:
            usuarios = self.usuario_repo.listar()

            for u in usuarios:
                if u[3] == "admin":
                    return  # ya existe admin

            password_hash = self.encriptar_password("admin")

            self.usuario_repo.agregar(
                "admin",
                password_hash,
                "admin",
                None
            )

            print("Admin inicial creado.")
            print("Usuario: admin")
            print("Password: admin")

        except Exception as e:
            print(f"Error creando admin inicial: {e}")


    def registrar_profesor(self, username, password, profesor_id):
        try:
            password_hash = self.encriptar_password(password)

            self.usuario_repo.agregar(
                username,
                password_hash,
                "profesor",
                profesor_id
            )

            return True, "Usuario profesor creado correctamente."

        except Exception as e:
            return False, f"Error creando usuario profesor: {e}"