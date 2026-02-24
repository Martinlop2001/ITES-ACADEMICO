


from repositorio.materia_repo import(
    agregar_materia,
    obtener_materia_por_nombre
)

def registrar_materia_servicio(nombre, profesor_id):
    if obtener_materia_por_nombre(nombre):
        return False, "ya existe una materia con ese nombre."

    if not nombre:
        return False, "El nombre es obligatorio!"

    agregar_materia(nombre, profesor_id)
    return True, "Materia agregada correctamente."

