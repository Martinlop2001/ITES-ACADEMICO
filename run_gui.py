


# run_gui.py - Se ejecuta para iniciar la interfaz gráfica PyQt6
import sys

from PyQt6.QtWidgets import QApplication

from db.database import crear_tablas, conectar
from repositorio.profesor_repo import ProfesorRepositorio
from repositorio.alumno_repo import AlumnoRepositorio
from repositorio.materia_repo import MateriaRepositorio
from repositorio.falta_repo import FaltaRepositorio
from repositorio.usuario_repo import UsuarioRepositorio
from servicios.profesor_servicio import ProfesorServicio
from servicios.alumno_servicio import AlumnoServicio
from servicios.materia_servicio import MateriaServicio
from servicios.falta_servicio import FaltaServicio
from servicios.usuario_servicio import UsuarioServicio
from servicios.email_servicio import EmailServicio
from ui.ventana_principal import VentanaPrincipal


def main():
    crear_tablas()
    conexion = conectar()

    profesor_repo = ProfesorRepositorio(conexion)
    alumno_repo = AlumnoRepositorio(conexion)
    materia_repo = MateriaRepositorio(conexion)
    falta_repo = FaltaRepositorio(conexion)
    usuario_repo = UsuarioRepositorio(conexion)

    profesor_servicio = ProfesorServicio(profesor_repo)
    alumno_servicio = AlumnoServicio(alumno_repo)
    materia_servicio = MateriaServicio(materia_repo)
    falta_servicio = FaltaServicio(falta_repo)
    usuario_servicio = UsuarioServicio(usuario_repo, alumno_servicio)

    usuario_servicio.crear_admin_inicial()

    email_servicio = EmailServicio.desde_env()

    app = QApplication(sys.argv)
    ventana = VentanaPrincipal(
        usuario_servicio=usuario_servicio,
        profesor_servicio=profesor_servicio,
        alumno_servicio=alumno_servicio,
        materia_servicio=materia_servicio,
        falta_servicio=falta_servicio,
        email_servicio=email_servicio,
    )
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
