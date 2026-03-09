


from PyQt6.QtWidgets import (
    QWidget, QTableWidgetItem, QHeaderView, QMessageBox, QDialog
)
from PyQt6.QtWidgets import QSizePolicy
from PyQt6 import uic

from ui.cargar_ui import ruta_ui
from ui.formulario_profesor import FormularioProfesor


class PantallaGestionProfesores(QWidget):
    
    #Gestión de profesores. Diseño en pantalla_gestion_profesores.ui.

    def __init__(self, ventana_principal, parent=None):
        super().__init__(parent)
        self.ventana = ventana_principal
        uic.loadUi(ruta_ui("pantalla_gestion_profesores.ui"), self)

        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.layout().setStretch(1, 1)  # tabla en índice 1

        self.btn_volver.clicked.connect(lambda: self.ventana.ir_a_gestion(2))
        self.btn_agregar.clicked.connect(self._agregar)
        self.btn_editar.clicked.connect(self._editar)
        self.btn_eliminar.clicked.connect(self._eliminar)

    def showEvent(self, event):
        super().showEvent(event)
        self._refrescar()

    def _refrescar(self):
        profesores = self.ventana.profesor_servicio.listar()
        self.tabla.setRowCount(len(profesores))
        for i, p in enumerate(profesores):
            self.tabla.setItem(i, 0, QTableWidgetItem(str(p[0])))
            self.tabla.setItem(i, 1, QTableWidgetItem(str(p[1])))
            self.tabla.setItem(i, 2, QTableWidgetItem(str(p[2])))
            self.tabla.setItem(i, 3, QTableWidgetItem(str(p[3])))
            self.tabla.setItem(i, 4, QTableWidgetItem(str(p[4])))

    def _agregar(self):
        d = FormularioProfesor(self)
        if d.exec() != QDialog.DialogCode.Accepted:
            return
        exito, msg = self.ventana.profesor_servicio.agregar(*d.obtener_datos())
        QMessageBox.information(self, "Profesores", msg)
        self._refrescar()

    def _editar(self):
        row = self.tabla.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Editar", "Selecciona una fila.")
            return
        id_val = self.tabla.item(row, 0).text()
        profesor = self.ventana.profesor_servicio.obtener_por_id(id_val)
        if not profesor:
            QMessageBox.warning(self, "Editar", "No se encontró el profesor.")
            return
        d = FormularioProfesor(self, datos=profesor)
        if d.exec() != QDialog.DialogCode.Accepted:
            return
        exito, msg = self.ventana.profesor_servicio.editar(id_val, *d.obtener_datos())
        QMessageBox.information(self, "Profesores", msg)
        self._refrescar()

    def _eliminar(self):
        row = self.tabla.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Eliminar", "Selecciona una fila.")
            return
        id_val = self.tabla.item(row, 0).text()
        profesor = self.ventana.profesor_servicio.obtener_por_id(id_val)
        if not profesor:
            return
        if QMessageBox.question(
            self, "Confirmar",
            f"¿Eliminar al profesor {profesor[2]} {profesor[3]} y todo lo asociado?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        ) != QMessageBox.StandardButton.Yes:
            return
        exito, msg = self.ventana.profesor_servicio.eliminar(id_val)
        QMessageBox.information(self, "Profesores", msg)
        self._refrescar()
