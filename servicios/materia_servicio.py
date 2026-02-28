



class MateriaServicio:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def agregar_materia(self, nombre, profesor_id):
        if not nombre:
            raise ValueError("El campo nombre no debe de estar vacio.")
        self.repositorio.agregar(nombre, profesor_id)

    def listar_materias(self):
        return self.repositorio.listar()

    def eliminar_materia(self, id):
        self.repositorio.eliminar(id)