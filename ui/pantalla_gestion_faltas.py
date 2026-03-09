


from PyQt6.QtWidgets import (
    QWidget, QTableWidgetItem, QHeaderView, QMessageBox, QDialog
)
from PyQt6.QtWidgets import QSizePolicy
from PyQt6 import uic

from ui.cargar_ui import ruta_ui
from ui.formulario_falta import FormularioFalta


class PantallaGestionFaltas(QWidget):
    #Gestión de faltas. Diseño en pantalla_gestion_faltas.ui.

    def __init__(self, ventana_principal, parent=None):
        super().__init__(parent)
        self.ventana = ventana_principal
        uic.loadUi(ruta_ui("pantalla_gestion_faltas.ui"), self)

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
        faltas = self.ventana.falta_servicio.listar_falta()
        self.tabla.setRowCount(len(faltas))
        for i, f in enumerate(faltas):
            self.tabla.setItem(i, 0, QTableWidgetItem(str(f[0])))
            self.tabla.setItem(i, 1, QTableWidgetItem(str(f[1])))
            self.tabla.setItem(i, 2, QTableWidgetItem(str(f[2])))
            self.tabla.setItem(i, 3, QTableWidgetItem(str(f[3])))
            self.tabla.setItem(i, 4, QTableWidgetItem(str(f[4])))

    def _agregar(self):
        d = FormularioFalta(self.ventana, self)
        if d.exec() != QDialog.DialogCode.Accepted:
            return
        datos = d.obtener_datos()
        exito, msg = self.ventana.falta_servicio.registrar_falta(*datos)
        QMessageBox.information(self, "Faltas", msg)
        if exito:
            self._enviar_email_falta(*datos)
        self._refrescar()

    def _enviar_email_falta(self, alumno_id, profesor_id, materia_id, fecha, motivo):
        email_servicio = getattr(self.ventana, "email_servicio", None)
        if email_servicio is None:
            return

        if not email_servicio.configurado():
            faltantes = []
            if not getattr(email_servicio, "enabled", False):
                faltantes.append("SMTP_ENABLED=True")
            if not getattr(email_servicio, "username", "").strip():
                faltantes.append("SMTP_USER")
            if not getattr(email_servicio, "password", "").strip():
                faltantes.append("SMTP_PASS")
            detalle = "Email no configurado o deshabilitado."
            if faltantes:
                detalle += " Verificá: " + ", ".join(faltantes)
            QMessageBox.warning(self, "Email", detalle)
            return

        # Obtener datos del alumno
        alumno = self.ventana.alumno_servicio.obtener_por_id(alumno_id)
        if not alumno:
            return
        alumno_correo = (alumno[4] or "").strip()
        if not alumno_correo:
            QMessageBox.warning(
                self, "Email",
                "No se pudo enviar el email: el alumno no tiene correo cargado."
            )
            return

        # Obtener nombres de profesor y materia para el mensaje
        profesor = self.ventana.profesor_servicio.obtener_por_id(profesor_id)
        profesor_nombre = f"{profesor[2]} {profesor[3]}".strip() if profesor else str(profesor_id)

        materia = self.ventana.materia_servicio.obtener_por_id(materia_id)
        materia_nombre = str(materia[1]) if materia else str(materia_id)

        alumno_nombre = f"{alumno[2]} {alumno[3]}".strip()

        asunto = f"Notificación de falta - {materia_nombre}"
        cuerpo = (
            f"Hola {alumno_nombre},\n\n"
            f"El administrador registró una falta en el sistema.\n\n"
            f"Profesor: {profesor_nombre}\n"
            f"Materia:  {materia_nombre}\n"
            f"Fecha:    {fecha}\n"
            f"Motivo:   {motivo}\n\n"
            "Este es un mensaje automático."
        )

        ok, detalle = email_servicio.enviar_texto(para=alumno_correo, asunto=asunto, cuerpo=cuerpo)
        if not ok:
            QMessageBox.warning(self, "Email", detalle)

    def _eliminar(self):
        row = self.tabla.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Eliminar", "Selecciona una fila.")
            return
        id_val = self.tabla.item(row, 0).text()
        if QMessageBox.question(
            self, "Confirmar",
            "¿Eliminar esta falta?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        ) != QMessageBox.StandardButton.Yes:
            return
        exito, msg = self.ventana.falta_servicio.eliminar_falta(id_val)
        QMessageBox.information(self, "Faltas", msg)
        self._refrescar()