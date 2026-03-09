


from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QDate
from PyQt6 import uic

from ui.cargar_ui import ruta_ui


class FormularioFalta(QDialog):

    #Diálogo registrar falta (admin). Diseño en formulario_falta.ui.
    def __init__(self, ventana_principal, parent=None):
        super().__init__(parent)
        self.ventana = ventana_principal
        uic.loadUi(ruta_ui("formulario_falta.ui"), self)

        flags = self.windowFlags()
        flags &= ~Qt.WindowType.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        self.setFixedSize(self.size())

        self.fecha.setDate(QDate.currentDate())
        self.fecha.setCalendarPopup(True)

        self.combo_alumno.addItem("-- Alumno --", None)
        for a in ventana_principal.alumno_servicio.listar():
            self.combo_alumno.addItem(f"{a[2]} {a[3]}", a[0])
        self.combo_profesor.addItem("-- Profesor --", None)
        for p in ventana_principal.profesor_servicio.listar():
            self.combo_profesor.addItem(f"{p[2]} {p[3]}", p[0])
        self.combo_materia.addItem("-- Materia --", None)
        for m in ventana_principal.materia_servicio.listar_materias():
            self.combo_materia.addItem(m[1], m[0])

        self.buttonBox.accepted.connect(self._ok)
        self.buttonBox.rejected.connect(self.reject)

    def _ok(self):
        if self.combo_alumno.currentData() is None:
            QMessageBox.warning(self, "Error", "Selecciona un alumno.")
            return
        if self.combo_profesor.currentData() is None:
            QMessageBox.warning(self, "Error", "Selecciona un profesor.")
            return
        if self.combo_materia.currentData() is None:
            QMessageBox.warning(self, "Error", "Selecciona una materia.")
            return
        if not self.input_motivo.text().strip():
            QMessageBox.warning(self, "Error", "Indica el motivo.")
            return
        self.accept()

    def obtener_datos(self):
        return (
            str(self.combo_alumno.currentData()),
            str(self.combo_profesor.currentData()),
            str(self.combo_materia.currentData()),
            self.fecha.date().toString("yyyy-MM-dd"),
            self.input_motivo.text().strip(),
        )
