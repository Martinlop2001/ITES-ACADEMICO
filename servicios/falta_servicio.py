



class FaltaServicio:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def registrar_falta(self, alumno_id, profesor_id, materia_id, fecha, motivo):
        try:
            if not alumno_id:
                return False, "El campo 'alumno_id' no puede estar vacio."
            if not profesor_id:
                return False, "El campo 'profesor_id' no puede estar vacio."
            if not materia_id:
                return False, "El campo 'materia_id' no puede estar vacio."
            if not fecha:
                return False, "El campo 'fecha' no puede estar vacio."
            if not motivo:
                return False, "El campo 'motivo' no puede estar vacio."
            self.repositorio.registrar(alumno_id, profesor_id, materia_id, fecha, motivo)
            return True, "Falta registrada correctamente."

        except Exception as e:
            return False, f"Ocurrio un error {e}"

    def listar_falta(self, alumno_id=None, profesor_id=None):
        try:
            if alumno_id:
                return self.repositorio.listar_por_alumno(alumno_id)
            if profesor_id is not None:
                return self.repositorio.listar_por_profesor(profesor_id)
            return self.repositorio.listar()
        except Exception as e:
            print(f"Error al listar faltas: {e}")
            return []

    def eliminar_falta(self, id):
        try:
            self.repositorio.eliminar(id)
            return True, "Falta eliminada correctamente."

        except Exception as e:
            return False, f"Ocurrio un error {e}"