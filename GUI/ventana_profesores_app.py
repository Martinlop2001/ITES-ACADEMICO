

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from ventana_profesores import Ui_Dialog  # Este es el archivo generado por pyuic5
import sys


class VentanaProfesores(QDialog):
    def __init__(self, ventana_principal):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btnAgregarProfesor.clicked.connect(self.agregar_profesor)
        self.ui.btnListaProfesores.clicked.connect(self.listar_profesores)
        self.ui.btnEliminarProfesor.clicked.connect(self.eliminar_profesor)

        self.ventana_principal = ventana_principal

        # Conectar botón "Volver al menú"
        self.ui.btnVolverMenu.clicked.connect(self.volver_al_menu)



    def volver_al_menu(self):
        self.ventana_principal.show()
        self.close()



    
    def agregar_profesor(self):
        nombre = self.ui.inputNombre.text()
        apellido = self.ui.inputApellido.text()
        dni = self.ui.inputDNI.text()
        correo = self.ui.inputCorreo.text()
        direccion = self.ui.inputDireccion.text()

        if not all([nombre, apellido, dni, correo, direccion]):
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Campos incompletos", "Por favor complete todos los campos.")
            return 
        
        from servicios import gestion_profesores
        gestion_profesores.agregar_profesor_gui(nombre, apellido, dni, correo, direccion)

        QMessageBox.information(self, "Éxito", "Profesor agregado correctamente.")
        self.limpiar_campos()

    

    def listar_profesores(self):
        from servicios import gestion_profesores
        profesores = gestion_profesores.obtener_profesores()

        mensaje = "Profesores registrados:\n\n"
        for p in profesores:
            mensaje += f"- {p[0]} {p[1]}\n- DNI: {p[2]}\n- Correo: {p[3]}\n\n"

        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(self, "Listado de Profesores", mensaje)




    def eliminar_profesor(self):
        dni = self.ui.inputDNI.text()

        if not dni:
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Error", "Ingrese el DNI del profesor a eliminar.")
            return

        from servicios import gestion_profesores
        exito = gestion_profesores.eliminar_profesor_por_dni(dni)

        if exito:
            QMessageBox.information(self, "Éxito", "Profesor eliminado correctamente.")
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Error", "No se encontró un profesor con ese DNI.")




    def limpiar_campos(self):
        self.ui.inputNombre.clear()
        self.ui.inputApellido.clear()
        self.ui.inputDNI.clear()
        self.ui.inputCorreo.clear()
        self.ui.inputDireccion.clear()


# Para testeo individual (opcional)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_dummy = QMainWindow()
    ventana = VentanaProfesores(ventana_dummy)
    ventana.show()
    sys.exit(app.exec_())