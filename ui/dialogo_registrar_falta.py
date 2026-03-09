


from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QDate
from PyQt6 import uic

from ui.cargar_ui import ruta_ui


class DialogoRegistrarFalta(QDialog):

    #Diálogo para registrar una falta (alumno, materia, fecha, motivo). Diseño en dialogo_registrar_falta.ui.

    def __init__(self, ventana_principal, parent=None):
        super().__init__(parent)
        self.ventana = ventana_principal
        uic.loadUi(ruta_ui("dialogo_registrar_falta.ui"), self)

        flags = self.windowFlags()
        flags &= ~Qt.WindowType.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        self.setFixedSize(self.size())

        self.fecha.setDate(QDate.currentDate())
        self.fecha.setCalendarPopup(True)

        alumnos = ventana_principal.alumno_servicio.listar()
        self._alumnos = [(a[0], f"{a[2]} {a[3]}") for a in alumnos]
        self.combo_alumno.addItem("-- Seleccionar alumno --", None)
        for id_a, texto in self._alumnos:
            self.combo_alumno.addItem(texto, id_a)

        profesor_id = ventana_principal.usuario_actual[4]
        materias = ventana_principal.materia_servicio.listar_materias_por_profesor(profesor_id)
        self._materias = [(m[0], m[1]) for m in materias]
        self.combo_materia.addItem("-- Seleccionar materia --", None)
        for id_m, nombre in self._materias:
            self.combo_materia.addItem(nombre, id_m)

        self.buttonBox.accepted.connect(self._aceptar)
        self.buttonBox.rejected.connect(self.reject)

    def _aceptar(self):
        alumno_id = self.combo_alumno.currentData()
        materia_id = self.combo_materia.currentData()
        motivo = self.input_motivo.text().strip()
        if alumno_id is None:
            QMessageBox.warning(self, "Error", "Selecciona un alumno.")
            return
        if materia_id is None:
            QMessageBox.warning(self, "Error", "Selecciona una materia.")
            return
        if not motivo:
            QMessageBox.warning(self, "Error", "Indica el motivo.")
            return
        self.accept()

    def obtener_datos(self):
        profesor_id = self.ventana.usuario_actual[4]
        fecha = self.fecha.date().toString("yyyy-MM-dd")
        return (
            str(self.combo_alumno.currentData()),
            str(profesor_id),
            str(self.combo_materia.currentData()),
            fecha,
            self.input_motivo.text().strip(),
        )
