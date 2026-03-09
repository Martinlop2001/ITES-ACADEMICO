


from PyQt6.QtWidgets import QDialog, QMessageBox, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6 import uic

from ui.cargar_ui import ruta_ui


class DialogoCrearUsuarioProfesor(QDialog):

    #Diálogo para crear usuario de profesor. Diseño en dialogo_crear_usuario_profesor.ui.

    def __init__(self, ventana_principal, parent=None):
        super().__init__(parent)
        self.ventana = ventana_principal
        uic.loadUi(ruta_ui("dialogo_crear_usuario_profesor.ui"), self)

        flags = self.windowFlags()
        flags &= ~Qt.WindowType.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        self.setFixedSize(self.size())

        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        profesores = ventana_principal.profesor_servicio.listar()
        self._profesores = [(p[0], f"{p[2]} {p[3]} - DNI {p[1]}") for p in profesores]
        self.combo_profesor.addItem("-- Seleccionar profesor --", None)
        for id_p, texto in self._profesores:
            self.combo_profesor.addItem(texto, id_p)

        self.buttonBox.accepted.connect(self._aceptar)
        self.buttonBox.rejected.connect(self.reject)

    def _aceptar(self):
        if self.combo_profesor.currentData() is None:
            QMessageBox.warning(self, "Error", "Selecciona un profesor.")
            return
        if not self.input_username.text().strip():
            QMessageBox.warning(self, "Error", "El usuario es obligatorio.")
            return
        if not self.input_password.text():
            QMessageBox.warning(self, "Error", "La contraseña es obligatoria.")
            return
        self.accept()

    def obtener_datos(self):
        return (
            str(self.combo_profesor.currentData()),
            self.input_username.text().strip(),
            self.input_password.text(),
        )
