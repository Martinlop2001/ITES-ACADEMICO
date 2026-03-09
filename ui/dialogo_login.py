


from PyQt6.QtWidgets import QDialog, QMessageBox, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6 import uic

from ui.cargar_ui import ruta_ui


class DialogoLogin(QDialog):
    #Diálogo para iniciar sesión. Diseño en dialogo_login.ui.

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(ruta_ui("dialogo_login.ui"), self)

        flags = self.windowFlags()
        flags &= ~Qt.WindowType.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        self.setFixedSize(self.size())

        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn_cancelar.clicked.connect(self.reject)
        self.btn_aceptar.clicked.connect(self._aceptar)

    def _aceptar(self):
        usuario = self.input_usuario.text().strip()
        password = self.input_password.text()
        if not usuario or not password:
            QMessageBox.warning(self, "Campos vacíos", "Completa usuario y contraseña.")
            return
        self.accept()

    def obtener_credenciales(self):
        return self.input_usuario.text().strip(), self.input_password.text()
