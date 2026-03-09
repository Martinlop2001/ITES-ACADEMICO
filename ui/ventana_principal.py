


from PyQt6.QtWidgets import (
    QMainWindow, QStackedWidget, QMessageBox, QDialog
)
from PyQt6.QtCore import Qt
from PyQt6 import uic

from ui.cargar_ui import ruta_ui
from ui.pantalla_inicio import PantallaInicio
from ui.pantalla_alumno import PantallaAlumno
from ui.pantalla_admin import PantallaAdmin
from ui.pantalla_profesor import PantallaProfesor
from ui.pantalla_gestion_profesores import PantallaGestionProfesores
from ui.pantalla_gestion_alumnos import PantallaGestionAlumnos
from ui.pantalla_gestion_materias import PantallaGestionMaterias
from ui.pantalla_gestion_faltas import PantallaGestionFaltas
from ui.dialogo_login import DialogoLogin
from ui.dialogo_registro import DialogoRegistro
from ui.dialogo_crear_usuario_profesor import DialogoCrearUsuarioProfesor


# Índices del QStackedWidget
INICIO = 0
ALUMNO = 1
ADMIN = 2
PROFESOR = 3
GESTION_PROFESORES = 4
GESTION_ALUMNOS = 5
GESTION_MATERIAS = 6
GESTION_FALTAS = 7


class VentanaPrincipal(QMainWindow):
    """Ventana principal: tamaño y mínimo desde .ui (p. ej. 800×800 / 400×400)."""

    def __init__(
        self,
        usuario_servicio,
        profesor_servicio,
        alumno_servicio,
        materia_servicio,
        falta_servicio,
        email_servicio=None,
        parent=None,
    ):
        super().__init__(parent)
        self.usuario_servicio = usuario_servicio
        self.profesor_servicio = profesor_servicio
        self.alumno_servicio = alumno_servicio
        self.materia_servicio = materia_servicio
        self.falta_servicio = falta_servicio
        self.email_servicio = email_servicio
        self.usuario_actual = None

        uic.loadUi(ruta_ui("ventana_principal.ui"), self)

        flags = self.windowFlags()
        flags &= ~Qt.WindowType.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        self.setFixedSize(self.size())

        # El .ui define centralwidget con un QStackedWidget "stack" dentro.
        self.stack = self.findChild(QStackedWidget, "stack")

        self.pantalla_inicio = PantallaInicio(self)
        self.pantalla_alumno = PantallaAlumno(self)
        self.pantalla_admin = PantallaAdmin(self)
        self.pantalla_profesor = PantallaProfesor(self)
        self.pantalla_gestion_profesores = PantallaGestionProfesores(self)
        self.pantalla_gestion_alumnos = PantallaGestionAlumnos(self)
        self.pantalla_gestion_materias = PantallaGestionMaterias(self)
        self.pantalla_gestion_faltas = PantallaGestionFaltas(self)

        self.stack.addWidget(self.pantalla_inicio)
        self.stack.addWidget(self.pantalla_alumno)
        self.stack.addWidget(self.pantalla_admin)
        self.stack.addWidget(self.pantalla_profesor)
        self.stack.addWidget(self.pantalla_gestion_profesores)
        self.stack.addWidget(self.pantalla_gestion_alumnos)
        self.stack.addWidget(self.pantalla_gestion_materias)
        self.stack.addWidget(self.pantalla_gestion_faltas)

        self._historial_indices = []
        self.stack.setCurrentIndex(INICIO)

    def _ir_a(self, indice, *, registrar_historial=True):
        actual = self.stack.currentIndex()
        if registrar_historial and actual != indice:
            self._historial_indices.append(actual)
        self.stack.setCurrentIndex(indice)

    def volver(self):
        if not self._historial_indices:
            return
        indice_anterior = self._historial_indices.pop()
        self._ir_a(indice_anterior, registrar_historial=False)

    def mostrar_login(self):
        d = DialogoLogin(self)
        if d.exec() != QDialog.DialogCode.Accepted:
            return
        usuario, password = d.obtener_credenciales()
        success, mensaje, usuario_obj = self.usuario_servicio.login(usuario, password)
        if not success:
            QMessageBox.warning(self, "Iniciar sesión", mensaje)
            return
        QMessageBox.information(self, "Iniciar sesión", mensaje)
        self.usuario_actual = usuario_obj
        rol = (usuario_obj[3] or "").strip().lower()
        if rol == "admin":
            self._ir_a(ADMIN)
        elif rol == "profesor":
            self._ir_a(PROFESOR)
        elif rol == "alumno":
            self._ir_a(ALUMNO)
        else:
            QMessageBox.warning(self, "Iniciar sesión", f"Rol no reconocido: {usuario_obj[3]!r}")
            return

    def mostrar_registro(self):
        d = DialogoRegistro(self)
        if d.exec() != QDialog.DialogCode.Accepted:
            return
        datos = d.obtener_datos()
        exito, mensaje = self.usuario_servicio.registrar_alumno(*datos)
        QMessageBox.information(self, "Registro", mensaje)

    def cerrar_aplicacion(self):
        self.close()

    def cerrar_sesion(self):
        self.usuario_actual = None
        self._historial_indices.clear()
        self._ir_a(INICIO, registrar_historial=False)

    def ir_a_gestion(self, indice):
        self._ir_a(indice)

    def mostrar_crear_usuario_profesor(self):
        d = DialogoCrearUsuarioProfesor(self)
        if d.exec() != QDialog.DialogCode.Accepted:
            return
        profesor_id, username, password = d.obtener_datos()
        exito, mensaje = self.usuario_servicio.registrar_profesor(username, password, profesor_id)
        QMessageBox.information(self, "Crear usuario profesor", mensaje)
