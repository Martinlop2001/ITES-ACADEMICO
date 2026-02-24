


from repositorio.profesor_repo import(
    agregar_profesor,
    obtener_profesor_por_dni,
)

def registrar_profesor_servicio(dni, nombre, apellido, correo):
    if obtener_profesor_por_dni(dni):
        return False, "Invalido, ya existe un profesor con ese DNI"

    if not dni or not nombre or not apellido:
        return False, "No se permiten campos vacios en DNI - Nomkbre - Apellido."

    agregar_profesor(dni, nombre, apellido, correo)

    return True, "Profesor agregado correctamente!"