


from repositorio.alumno_repo import(
    agregar_alumno,
    obtener_alumno_por_dni,
)

def registrar_alumno_servicio(dni, nombre, apellido, correo):
    if obtener_alumno_por_dni(dni):
        return False, "Invalido, ya existe un alumno con ese DNI"

    if not dni or not nombre or not apellido:
        return False, "No se permiten campos vacios en DNI - Nomkbre - Apellido."

    agregar_alumno(dni, nombre, apellido, correo)

    return True, "Alumno agregado correctamente!"