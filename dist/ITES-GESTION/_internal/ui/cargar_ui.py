


#Ruta base para archivos .ui de Qt Designer (ui/forms/).
import os

_DIR_UI = os.path.dirname(os.path.abspath(__file__))
FORMS_DIR = os.path.join(_DIR_UI, "forms")


def ruta_ui(nombre_archivo: str) -> str:
    #Devuelve la ruta absoluta a un archivo .ui en ui/forms/.
    if not nombre_archivo.endswith(".ui"):
        nombre_archivo += ".ui"
    return os.path.join(FORMS_DIR, nombre_archivo)
