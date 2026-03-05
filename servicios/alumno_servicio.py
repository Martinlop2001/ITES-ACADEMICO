



class AlumnoServicio:
    def __init__(self, alumno_repo):
        self.alumno_repo = alumno_repo
    
    def agregar(self, dni, nombre, apellido, correo):

        try:
            if not dni or not nombre or not apellido:
                return False, "No se permiten campos vacios en DNI - Nombre - Apellido."
            
            alumnos = self.alumno_repo.listar()

            for a in alumnos:
                if a[1] == dni:
                    return False, "Ya existe un alumno con ese mismo DNI..."

            self.alumno_repo.agregar(dni, nombre, apellido, correo)
            return True, "Alumno agregado correctamente."

        except Exception as a:
            return False, f"Ocurrio un error. {a}"
    
    def listar(self):
        return self.alumno_repo.listar()

    def editar(self, id, dni, nombre, apellido, correo):
        return self.alumno_repo.editar(id, dni, nombre, apellido, correo)

    def eliminar(self, id):
        return self.alumno_repo.eliminar(id)
    