


from PyQt6.QtWidgets import QDialog, QMessageBox, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6 import uic

from ui.cargar_ui import ruta_ui


class DialogoRegistro(QDialog):

    #Diálogo para registrarse como alumno. Diseño en dialogo_registro.ui.

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(ruta_ui("dialogo_registro.ui"), self)

        flags = self.windowFlags()
        flags &= ~Qt.WindowType.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        self.setFixedSize(self.size())

        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn_cancelar.clicked.connect(self.reject)
        self.btn_aceptar.clicked.connect(self._aceptar)

    def _aceptar(self):
        if not self.input_dni.text().strip():
            QMessageBox.warning(self, "Campo vacío", "El DNI es obligatorio.")
            return
        if not self.input_nombre.text().strip():
            QMessageBox.warning(self, "Campo vacío", "El nombre es obligatorio.")
            return
        if not self.input_apellido.text().strip():
            QMessageBox.warning(self, "Campo vacío", "El apellido es obligatorio.")
            return
        if not self.input_correo.text().strip():
            QMessageBox.warning(self, "Campo vacío", "El correo es obligatorio.")
            return
        if not self.input_username.text().strip():
            QMessageBox.warning(self, "Campo vacío", "El usuario es obligatorio.")
            return
        if not self.input_password.text():
            QMessageBox.warning(self, "Campo vacío", "La contraseña es obligatoria.")
            return
        self.accept()

    def obtener_datos(self):
        return (
            self.input_dni.text().strip(),
            self.input_nombre.text().strip(),
            self.input_apellido.text().strip(),
            self.input_correo.text().strip(),
            self.input_username.text().strip(),
            self.input_password.text(),
        )
