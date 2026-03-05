



class FaltaServicio:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def registrar_falta(self, profesor_id, materia_id, fecha, motivo):
        try:
            if not profesor_id:
                return False, "El campo 'profesor_id' no puede estar vacio."

            if not materia_id:
                return False, "El campo 'materia_id' no puede estar vacio."

            if not fecha:
                return False, "El campo 'fecha' no puede estar vacio."

            if not motivo:
                return False, "El campo 'motivo' no puede estar vacio."

            self.repositorio.registrar(profesor_id, materia_id, fecha, motivo)
            return True, "Falta registrada correctamente."
        except Exception as e:
            return False, f"Ocurrio un error {e}"

    def listar_falta(self):
        return self.repositorio.listar()

    def eliminar_falta(self, id):
        try:
            self.repositorio.eliminar(id)
            return True, "Falta eliminada correctamente."
        except Exception as e:
            return False, f"Ocurrio un error {e}"