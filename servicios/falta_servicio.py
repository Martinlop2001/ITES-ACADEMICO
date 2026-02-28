


class FaltaServicio:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def registrar_falta(self, profesor_id, materia_id, fecha, motivo):

        if not fecha:
            raise ValueError("El campo 'fecha' no puede estar vacio.")

        if not motivo:
            raise ValueError("El campo 'motivo' no puede estar vacio.")

        self.repositorio.registrar(profesor_id, materia_id, fecha, motivo)

    def listar_falta(self):
        return self.repositorio.listar()

    def eliminar_falta(self, id):
        self.repositorio.eliminar(id)