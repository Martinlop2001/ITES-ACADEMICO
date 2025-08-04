

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow
from ventana_profesores_app import VentanaProfesores

# Importamos tus módulos reales
from servicios import gestion_profesores
from servicios import gestion_alumnos
from servicios import gestion_materias
from servicios import faltas


class ItesAcademicoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar botones a funciones reales
        self.ui.btnProfesores.clicked.connect(self.abrir_gestion_profesores)
        self.ui.btnAlumnos.clicked.connect(self.abrir_gestion_alumnos)
        self.ui.btnMaterias.clicked.connect(self.abrir_gestion_materias)
        self.ui.btnRegistrarFalta.clicked.connect(self.registrar_falta)
        self.ui.btnConsultarFaltas.clicked.connect(self.consultar_faltas)
        self.ui.btnSalir.clicked.connect(self.close)

    def abrir_gestion_profesores(self):
        self.ventana_profesores = VentanaProfesores(self)
        self.ventana_profesores.show()
        self.hide()

    def abrir_gestion_alumnos(self):
        gestion_alumnos.menu_interactivo()

    def abrir_gestion_materias(self):
        gestion_materias.menu_interactivo()

    def registrar_falta(self):
        faltas.registrar_falta()

    def consultar_faltas(self):
        faltas.listar_faltas()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ItesAcademicoApp()
    ventana.show()
    sys.exit(app.exec_())
