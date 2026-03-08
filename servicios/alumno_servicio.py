



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
        try:
            self.alumno_repo.editar(id, dni, nombre, apellido, correo)
            return True, "Datos editados correctamente."
        except Exception as e:
            return False, f"Ocurrio un error al editar alumno: {e}"

    def eliminar(self, id):
        try:
            self.alumno_repo.eliminar(id)
            return True, "Alumno eliminado correctamente."
        except Exception as e:
            return False, f"No se pudo eliminar el alumno. Verifique que no tenga faltas asociadas. Detalle: {e}"
    
    def obtener_por_dni(self, dni):
        return self.alumno_repo.obtener_por_dni(dni)
    
    def obtener_por_id(self, id):
        return self.alumno_repo.obtener_por_id(id)