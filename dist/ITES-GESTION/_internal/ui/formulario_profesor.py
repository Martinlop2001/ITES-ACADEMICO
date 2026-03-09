


from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6 import uic

from ui.cargar_ui import ruta_ui


class FormularioProfesor(QDialog):
    
    #Diálogo agregar/editar profesor. Diseño en formulario_profesor.ui.

    def __init__(self, parent=None, datos=None):
        super().__init__(parent)
        uic.loadUi(ruta_ui("formulario_profesor.ui"), self)

        flags = self.windowFlags()
        flags &= ~Qt.WindowType.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        self.setFixedSize(self.size())

        self._datos = datos
        if datos:
            self.setWindowTitle("Editar profesor")
            self.input_dni.setText(str(datos[1]))
            self.input_nombre.setText(str(datos[2]))
            self.input_apellido.setText(str(datos[3]))
            self.input_correo.setText(str(datos[4]))
        else:
            self.setWindowTitle("Agregar profesor")

        self.buttonBox.accepted.connect(self._ok)
        self.buttonBox.rejected.connect(self.reject)

    def _ok(self):
        if not self.input_dni.text().strip():
            QMessageBox.warning(self, "Error", "DNI obligatorio.")
            return
        if not self.input_nombre.text().strip():
            QMessageBox.warning(self, "Error", "Nombre obligatorio.")
            return
        if not self.input_apellido.text().strip():
            QMessageBox.warning(self, "Error", "Apellido obligatorio.")
            return
        if not self.input_correo.text().strip():
            QMessageBox.warning(self, "Error", "Correo obligatorio.")
            return
        self.accept()

    def obtener_datos(self):
        return (
            self.input_dni.text().strip(),
            self.input_nombre.text().strip(),
            self.input_apellido.text().strip(),
            self.input_correo.text().strip(),
        )
