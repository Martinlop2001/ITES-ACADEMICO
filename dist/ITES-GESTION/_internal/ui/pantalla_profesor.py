


import os
from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QMessageBox, QDialog, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6 import uic

from PyQt6.QtWidgets import QMessageBox

from ui.cargar_ui import ruta_ui
from ui.dialogo_registrar_falta import DialogoRegistrarFalta


class PantallaProfesor(QWidget):
    
    #Menú profesor: Registrar falta, Ver mis faltas, Cerrar sesión. Diseño en pantalla_profesor.ui.

    def __init__(self, ventana_principal, parent=None):
        super().__init__(parent)
        self.ventana = ventana_principal
        uic.loadUi(ruta_ui("pantalla_profesor.ui"), self)

        self._cargar_fondo()

        self.tabla_faltas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_faltas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.btn_volver.clicked.connect(self._volver_menu)


        self.btn_registrar.clicked.connect(self._registrar_falta)
        self.btn_ver_faltas.clicked.connect(self._toggle_ver_faltas)
        self.btn_cerrar.clicked.connect(self.ventana.cerrar_sesion)

    def _mostrar_menu(self, mostrar: bool):
        self.btn_registrar.setVisible(mostrar)
        self.btn_ver_faltas.setVisible(mostrar)
        self.tabla_faltas.setVisible(not mostrar)

    def _volver_menu(self):
        self._mostrar_menu(True)

    def _toggle_ver_faltas(self):
        if self.tabla_faltas.isVisible():
            self._mostrar_menu(True)
            return
        self._ver_faltas()

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
        return os.path.join(base, "assets", "fondo_profesor.jpg")

    def _registrar_falta(self):
        d = DialogoRegistrarFalta(self.ventana, self)
        if d.exec() != QDialog.DialogCode.Accepted:
            return
        datos = d.obtener_datos()
        exito, msg = self.ventana.falta_servicio.registrar_falta(*datos)
        QMessageBox.information(self, "Registrar falta", msg)
        if exito:
            self._enviar_email_falta(*datos)
            self._ver_faltas()

    def _enviar_email_falta(self, alumno_id, profesor_id, materia_id, fecha, motivo):
        email_servicio = getattr(self.ventana, "email_servicio", None)
        if email_servicio is None:
            QMessageBox.warning(
                self,
                "Email",
                "No se pudo enviar el email porque el servicio de email no está disponible en la aplicación.",
            )
            return

        if not email_servicio.configurado():
            faltantes = []
            if not getattr(email_servicio, "enabled", False):
                faltantes.append("ITES_EMAIL_ENABLED=1")
            if not getattr(email_servicio, "username", "").strip():
                faltantes.append("ITES_SMTP_USER")
            if not getattr(email_servicio, "password", "").strip():
                faltantes.append("ITES_SMTP_PASS")

            detalle = "Email no configurado o deshabilitado."
            if faltantes:
                detalle += " Faltan/Verifica: " + ", ".join(faltantes)
            QMessageBox.warning(self, "Email", detalle)
            return

        alumno = self.ventana.alumno_servicio.obtener_por_id(alumno_id)
        if not alumno:
            return
        alumno_correo = (alumno[4] or "").strip()
        if not alumno_correo:
            QMessageBox.warning(
                self,
                "Email",
                "No se pudo enviar el email porque el alumno no tiene un correo cargado.",
            )
            return

        profesor = self.ventana.profesor_servicio.obtener_por_id(profesor_id)
        profesor_nombre = ""
        if profesor:
            profesor_nombre = f"{profesor[2]} {profesor[3]}".strip()

        materia = self.ventana.materia_servicio.obtener_por_id(materia_id)
        materia_nombre = ""
        if materia:
            materia_nombre = str(materia[1])

        alumno_nombre = f"{alumno[2]} {alumno[3]}".strip()

        asunto = "Notificación de falta"
        if materia_nombre:
            asunto = f"Notificación de falta - {materia_nombre}"

        cuerpo = (
            f"Hola {alumno_nombre},\n\n"
            f"Se registró una falta/asistencia en el sistema.\n\n"
            f"Profesor: {profesor_nombre or profesor_id}\n"
            f"Materia: {materia_nombre or materia_id}\n"
            f"Fecha: {fecha}\n"
            f"Motivo: {motivo}\n\n"
            "Este es un mensaje automático."
        )

        ok, detalle = email_servicio.enviar_texto(para=alumno_correo, asunto=asunto, cuerpo=cuerpo)
        if not ok:
            QMessageBox.warning(self, "Email", detalle)

    def _ver_faltas(self):
        profesor_id = self.ventana.usuario_actual[4]
        faltas = self.ventana.falta_servicio.listar_falta(profesor_id=profesor_id)
        self.tabla_faltas.setRowCount(len(faltas))
        for i, f in enumerate(faltas):
            self.tabla_faltas.setItem(i, 0, QTableWidgetItem(str(f[0])))
            self.tabla_faltas.setItem(i, 1, QTableWidgetItem(str(f[1])))
            self.tabla_faltas.setItem(i, 2, QTableWidgetItem(str(f[2])))
            self.tabla_faltas.setItem(i, 3, QTableWidgetItem(str(f[3])))
            self.tabla_faltas.setItem(i, 4, QTableWidgetItem(str(f[4])))
        self._mostrar_menu(False)