class MateriaServicio:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def agregar_materia(self, nombre, profesor_id):
        try:
            if not nombre:
                return False, "El campo nombre no debe de estar vacio."
            if not profesor_id:
                return False, "El campo profesor_id no debe de estar vacio."

            self.repositorio.agregar(nombre, profesor_id)
            return True, "Materia registrada correctamente."
        except Exception as e:
            return False, f"Ocurrio un error {e}"

    def listar_materias(self):
        return self.repositorio.listar()

    def listar_materias_por_profesor(self, profesor_id):
        return self.repositorio.listar_por_profesor(profesor_id)

    def obtener_por_id(self, id):
        return self.repositorio.obtener_por_id(id)

    def eliminar_materia(self, id):
        try:
            self.repositorio.eliminar(id)
            return True, "Materia eliminada correctamente."
        except Exception as e:
            return False, f"Ocurrio un error {e}"