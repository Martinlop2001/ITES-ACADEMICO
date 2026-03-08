



class ProfesorServicio:
    def __init__(self, profesor_repo):
        self.profesor_repo = profesor_repo

    def agregar(self, dni, nombre, apellido, correo):

        try:
            if not dni or not nombre or not apellido:
                return False, "No se permiten campos vacios en DNI - Nombre - Apellido."
            
            profesores = self.profesor_repo.listar()

            for p in profesores:
                if p[1] == dni:
                    return False, "Ya existe un profesor con ese mismo DNI..."

            self.profesor_repo.agregar(dni, nombre, apellido, correo)
            return True, "Profesor registrado correctamente."

        except Exception as e:
            return False, f"Ocurrio un error {e}"
    
    def listar(self):
        return self.profesor_repo.listar()

    def editar(self, id, dni, nombre, apellido, correo):
        try:
            self.profesor_repo.editar(id, dni, nombre, apellido, correo)
            return True, "Datos editados correctamente."
        except Exception as e:
            return False, f"Ocurrio un error al editar profesor: {e}"
    
    def eliminar(self, id):
        try:
            self.profesor_repo.eliminar(id)
            return True, "Profesor eliminado correctamente."
        except Exception as e:
            return False, f"No se pudo eliminar el profesor. Verifique que no tenga materias o faltas asociadas. Detalle: {e}"

    def obtener_por_id(self, id):
        return self.profesor_repo.obtener_por_id(id)