

from repositorio.falta_repo import (
    registrar_falta,
    obtener_falta_por_materia_y_fecha,
    obtener_materia_por_id
)

def registrar_falta_servicio(materia_id, fecha, motivo):
    if not obtener_materia_por_id(materia_id):
        return False, "La materia no existe."

    if obtener_falta_por_materia_y_fecha(materia_id, fecha):
        return False, "Ya existe una falta registrada para esa materia en la misma fecha."

    registrar_falta(materia_id, fecha, motivo)
    return True, "Falta registrada correctamente."