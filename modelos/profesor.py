

from modelos.persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, dni, correo, direccion):
        super().__init__(nombre, apellido, dni, correo, direccion)