



class ProfesorServicio:
    def __init__(self, profesor_repo):
        self.profesor_repo = profesor_repo

    def agregar(self, dni, nombre, apellido, correo):

        try:
            if not dni or not nombre or not apellido:
                return False, "No se permiten campos vacios en DNI - Nomkbre - Apellido."
            
            profesores = self.profesor_repo.listar()

            for p in profesores:
                if p[1] == dni:
                    return False, "Ya existe un profesor con ese mismo DNI..."

            self.profesor_repo.agregar(dni, nombre, apellido, correo)
            return True, "Profesor registrado correctamente."

        except Exception as e:
            return False, f"Ocurrio un error {e}"
