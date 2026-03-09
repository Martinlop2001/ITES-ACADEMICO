


import os
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap
from PyQt6 import uic

from ui.cargar_ui import ruta_ui


class PantallaAdmin(QWidget):

    #Menú admin. Diseño en pantalla_admin.ui.

    def __init__(self, ventana_principal, parent=None):
        super().__init__(parent)
        self.ventana = ventana_principal
        uic.loadUi(ruta_ui("pantalla_admin.ui"), self)

        self._cargar_fondo()

        self.btn_profesores.clicked.connect(lambda: self.ventana.ir_a_gestion(4))
        self.btn_alumnos.clicked.connect(lambda: self.ventana.ir_a_gestion(5))
        self.btn_materias.clicked.connect(lambda: self.ventana.ir_a_gestion(6))
        self.btn_faltas.clicked.connect(lambda: self.ventana.ir_a_gestion(7))
        self.btn_crear_profesor.clicked.connect(self.ventana.mostrar_crear_usuario_profesor)
        self.btn_cerrar.clicked.connect(self.ventana.cerrar_sesion)

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
        return os.path.join(base, "assets", "fondo_admin.jpg")
