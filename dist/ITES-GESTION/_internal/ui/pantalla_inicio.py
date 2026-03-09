


import os
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap
from PyQt6 import uic

from ui.cargar_ui import ruta_ui


class PantallaInicio(QWidget):

    #Pantalla principal: título, fondo opcional, botones. Diseño en pantalla_inicio.ui.

    def __init__(self, ventana_principal, parent=None):
        super().__init__(parent)
        self.ventana = ventana_principal
        uic.loadUi(ruta_ui("pantalla_inicio.ui"), self)

        # Cargar imagen de fondo en lbl_fondo
        ruta_fondo = self._ruta_fondo()
        if os.path.isfile(ruta_fondo):
            pixmap = QPixmap(ruta_fondo).scaled(
                self.width(), self.height()
            )
            self.lbl_fondo.setPixmap(pixmap)

        self.btn_iniciar.clicked.connect(self.ventana.mostrar_login)
        self.btn_registrarse.clicked.connect(self.ventana.mostrar_registro)
        self.btn_salir.clicked.connect(self.ventana.cerrar_aplicacion)

    def resizeEvent(self, event):

        #Escalar el fondo si la ventana cambia de tamaño.
        super().resizeEvent(event)
        ruta_fondo = self._ruta_fondo()
        if os.path.isfile(ruta_fondo):
            pixmap = QPixmap(ruta_fondo).scaled(
                self.width(), self.height()
            )
            self.lbl_fondo.setPixmap(pixmap)
            self.lbl_fondo.resize(self.width(), self.height())

    def _ruta_fondo(self):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base, "assets", "fondo_inicio.jpg")