

from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from GUI.ventana_profesores import Ui_Dialog
from servicios import gestion_profesores

class VentanaProfesores(QDialog):
    def __init__(self, ventana_anterior=None):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ventana_anterior = ventana_anterior

        # Conectar botones
        self.ui.btnAgregarProfesor.clicked.connect(self.agregar_profesor)
        self.ui.btnListarProfesores.clicked.connect(self.listar_profesores)
        self.ui.btnVolver.clicked.connect(self.volver_al_menu)

    def agregar_profesor(self):
        nombre = self.ui.inputNombre.text()
        apellido = self.ui.inputApellido.text()
        dni = self.ui.inputDNI.text()
        correo = self.ui.inputCorreo.text()
        direccion = self.ui.inputDireccion.text()

        if not all([nombre, apellido, dni, correo, direccion]):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        gestion_profesores.agregar_profesor_gui(nombre, apellido, dni, correo, direccion)
        QMessageBox.information(self, "Éxito", "Profesor agregado correctamente.")
        self.limpiar_campos()

    def listar_profesores(self):
        profesores = gestion_profesores.obtener_profesores()
        self.ui.tablaProfesores.setRowCount(0)

        for fila, profe in enumerate(profesores):
            self.ui.tablaProfesores.insertRow(fila)
            for columna, valor in enumerate(profe):
                self.ui.tablaProfesores.setItem(fila, columna, QTableWidgetItem(str(valor)))

    def limpiar_campos(self):
        self.ui.inputNombre.clear()
        self.ui.inputApellido.clear()
        self.ui.inputDNI.clear()
        self.ui.inputCorreo.clear()
        self.ui.inputDireccion.clear()

    def volver_al_menu(self):
        self.close()
        if self.ventana_anterior:
            self.ventana_anterior.show()
