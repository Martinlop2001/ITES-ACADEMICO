


import os
from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QMessageBox, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6 import uic

from ui.cargar_ui import ruta_ui


class PantallaAlumno(QWidget):

    #Menú alumno: Consultar mis faltas, Cerrar sesión. Diseño en pantalla_alumno.ui.

    def __init__(self, ventana_principal, parent=None):
        super().__init__(parent)
        self.ventana = ventana_principal
        uic.loadUi(ruta_ui("pantalla_alumno.ui"), self)

        self._cargar_fondo()

        self.tabla_faltas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_faltas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


        self.btn_volver.clicked.connect(self._volver_menu)

        self.btn_faltas.clicked.connect(self._consultar_faltas)
        self.btn_cerrar.clicked.connect(self.ventana.cerrar_sesion)

    def _mostrar_menu(self, mostrar: bool):
        self.btn_faltas.setVisible(mostrar)
        self.tabla_faltas.setVisible(not mostrar)

    def _volver_menu(self):
        self._mostrar_menu(True)

    def _cargar_fondo(self):
        ruta = self._ruta_fondo()
        if os.path.isfile(ruta):
            pixmap = QPixmap(ruta).scaled(self.width(), self.height())
            self.lbl_fondo.setPixmap(pixmap)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._cargar_fondo()
        self.lbl_fondo.resize(self.width(), self.height())

    def _ruta_fondo(self):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base, "assets", "fondo_alumno.jpg")

    def _consultar_faltas(self):
        if self.tabla_faltas.isVisible():
            self._mostrar_menu(True)
            return
        usuario = self.ventana.usuario_actual
        if not usuario:
            return
        alumno_id = usuario[4]
        faltas = self.ventana.falta_servicio.listar_falta(alumno_id=alumno_id)
        self.tabla_faltas.setRowCount(len(faltas))
        for i, f in enumerate(faltas):
            self.tabla_faltas.setItem(i, 0, QTableWidgetItem(str(f[0])))
            self.tabla_faltas.setItem(i, 1, QTableWidgetItem(str(f[1])))
            self.tabla_faltas.setItem(i, 2, QTableWidgetItem(str(f[2])))
            self.tabla_faltas.setItem(i, 3, QTableWidgetItem(str(f[3])))
        self._mostrar_menu(False)
        if not faltas:
            QMessageBox.information(self, "Faltas", "No tenés faltas registradas.")
