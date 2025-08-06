

from PyQt5.QtWidgets import QDialog
from eliminar_profesor import Ui_Dialog  # Clase generada por pyuic5
from servicios.gestion_profesores import listar_profesores, eliminar_profesor


class VentanaEliminarProfesor(QDialog):
    def __init__(self, ventana_anterior):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ventana_anterior = ventana_anterior

        # Listar profesores al iniciar la ventana
        self.mostrar_profesores()

        # Conectar botones
        self.ui.btnEliminar.clicked.connect(self.eliminar)
        self.ui.btnVolver.clicked.connect(self.volver)

    def mostrar_profesores(self):
        profesores = listar_profesores()
        texto = ""
        for profe in profesores:
            texto += f"ID: {profe[0]} | Nombre: {profe[1]} {profe[2]} | DNI: {profe[3]} | Correo: {profe[4]} | Dirección: {profe[5]}\n"
        self.ui.textEdit.setPlainText(texto)

    def eliminar(self):
        id_str = self.ui.inputID.text()
        if id_str.isdigit():
            id_profesor = int(id_str)
            eliminar_profesor(id_profesor)
            self.mostrar_profesores()
            self.ui.inputID.clear()

    def volver(self):
        self.ventana_anterior.show()
        self.close()