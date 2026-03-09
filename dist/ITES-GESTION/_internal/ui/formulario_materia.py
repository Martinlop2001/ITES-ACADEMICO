


from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6 import uic

from ui.cargar_ui import ruta_ui


class FormularioMateria(QDialog):
    
    #Diálogo agregar materia. Diseño en formulario_materia.ui.

    def __init__(self, ventana_principal, parent=None):
        super().__init__(parent)
        self.ventana = ventana_principal
        uic.loadUi(ruta_ui("formulario_materia.ui"), self)

        flags = self.windowFlags()
        flags &= ~Qt.WindowType.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        self.setFixedSize(self.size())

        self.combo_profesor.addItem("-- Seleccionar profesor --", None)
        for p in ventana_principal.profesor_servicio.listar():
            self.combo_profesor.addItem(f"{p[2]} {p[3]}", p[0])

        self.buttonBox.accepted.connect(self._ok)
        self.buttonBox.rejected.connect(self.reject)

    def _ok(self):
        if not self.input_nombre.text().strip():
            QMessageBox.warning(self, "Error", "Nombre obligatorio.")
            return
        if self.combo_profesor.currentData() is None:
            QMessageBox.warning(self, "Error", "Selecciona un profesor.")
            return
        self.accept()

    def obtener_datos(self):
        return (
            self.input_nombre.text().strip(),
            str(self.combo_profesor.currentData()),
        )
