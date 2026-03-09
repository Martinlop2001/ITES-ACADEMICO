


from PyQt6.QtWidgets import (
    QWidget, QTableWidgetItem, QHeaderView, QMessageBox, QDialog
)
from PyQt6.QtWidgets import QSizePolicy
from PyQt6 import uic

from ui.cargar_ui import ruta_ui
from ui.formulario_materia import FormularioMateria


class PantallaGestionMaterias(QWidget):

    #Gestión de materias. Diseño en pantalla_gestion_materias.ui.
    def __init__(self, ventana_principal, parent=None):
        super().__init__(parent)
        self.ventana = ventana_principal
        uic.loadUi(ruta_ui("pantalla_gestion_materias.ui"), self)

        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.layout().setStretch(1, 1)

        self.btn_volver.clicked.connect(lambda: self.ventana.ir_a_gestion(2))
        self.btn_agregar.clicked.connect(self._agregar)
        self.btn_eliminar.clicked.connect(self._eliminar)

    def showEvent(self, event):
        super().showEvent(event)
        self._refrescar()

    def _refrescar(self):
        materias = self.ventana.materia_servicio.listar_materias()
        self.tabla.setRowCount(len(materias))
        for i, m in enumerate(materias):
            self.tabla.setItem(i, 0, QTableWidgetItem(str(m[0])))
            self.tabla.setItem(i, 1, QTableWidgetItem(str(m[1])))
            self.tabla.setItem(i, 2, QTableWidgetItem(str(m[2])))
            self.tabla.setItem(i, 3, QTableWidgetItem(str(m[3])))

    def _agregar(self):
        d = FormularioMateria(self.ventana, self)
        if d.exec() != QDialog.DialogCode.Accepted:
            return
        exito, msg = self.ventana.materia_servicio.agregar_materia(*d.obtener_datos())
        QMessageBox.information(self, "Materias", msg)
        self._refrescar()

    def _eliminar(self):
        row = self.tabla.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Eliminar", "Selecciona una fila.")
            return
        id_val = self.tabla.item(row, 0).text()
        nombre = self.tabla.item(row, 1).text()
        if QMessageBox.question(
            self, "Confirmar",
            f"¿Eliminar la materia '{nombre}' y todas sus faltas?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        ) != QMessageBox.StandardButton.Yes:
            return
        exito, msg = self.ventana.materia_servicio.eliminar_materia(id_val)
        QMessageBox.information(self, "Materias", msg)
        self._refrescar()
