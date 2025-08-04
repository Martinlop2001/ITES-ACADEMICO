

import sqlite3
from database.conexion import conectar
from modelos.profesor import Profesor

def agregar_profesor():
    print("\n--- Agregar Profesor ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    correo = input("Correo: ")
    direccion = input("Dirección: ")

    profesor = Profesor(nombre, apellido, dni, correo, direccion)

    conexion = conectar()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            INSERT INTO profesor (nombre, apellido, dni, correo, direccion)
            VALUES (?, ?, ?, ?, ?)
        """, (profesor.nombre, profesor.apellido, profesor.dni, profesor.correo, profesor.direccion))
        conexion.commit()
        print("Profesor agregado correctamente.")
    except Exception as e:
        print("Error al agregar profesor:", e)
    finally:
        conexion.close()

def listar_profesores():
    print("\n--- Lista de Profesores ---")
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, apellido, dni, correo, direccion FROM profesor")
    profesores = cursor.fetchall()

    if profesores:
        for p in profesores:
            print(f"[{p[0]}] {p[1]} {p[2]} - DNI: {p[3]} - Correo: {p[4]} - Dirección: {p[5]}")
    else:
        print("No hay profesores registrados.")

    conexion.close()

def editar_profesor():
    listar_profesores()
    profesor_id = input("Ingrese el ID del profesor a editar: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre, apellido, dni, correo, direccion FROM profesor WHERE id = ?", (profesor_id,))
    profesor = cursor.fetchone()

    if not profesor:
        print("Profesor no encontrado.")
        conexion.close()
        return

    print("Deje vacío para no modificar.")

    nombre = input(f"Nombre [{profesor[0]}]: ") or profesor[0]
    apellido = input(f"Apellido [{profesor[1]}]: ") or profesor[1]
    dni = input(f"DNI [{profesor[2]}]: ") or profesor[2]
    correo = input(f"Correo [{profesor[3]}]: ") or profesor[3]
    direccion = input(f"Dirección [{profesor[4]}]: ") or profesor[4]

    try:
        cursor.execute("""
            UPDATE profesor
            SET nombre = ?, apellido = ?, dni = ?, correo = ?, direccion = ?
            WHERE id = ?
        """, (nombre, apellido, dni, correo, direccion, profesor_id))
        conexion.commit()
        print("Profesor actualizado correctamente.")
    except Exception as e:
        print("Error al actualizar profesor:", e)
    finally:
        conexion.close()

def eliminar_profesor():
    listar_profesores()
    profesor_id = input("Ingrese el ID del profesor a eliminar: ")

    confirmacion = input(f"¿Está seguro que desea eliminar al profesor con ID {profesor_id}? (s/n): ")
    if confirmacion.lower() != 's':
        print("Eliminación cancelada.")
        return

    conexion = conectar()
    cursor = conexion.cursor()

    try:
        cursor.execute("DELETE FROM profesor WHERE id = ?", (profesor_id,))
        conexion.commit()
        print("Profesor eliminado correctamente.")
    except Exception as e:
        print("Error al eliminar profesor:", e)
    finally:
        conexion.close()



def menu_interactivo():
    while True:
        print("\n--- Gestión de Profesores ---")
        print("1. Agregar profesor")
        print("2. Listar profesores")
        print("3. Editar profesor")
        print("4. Eliminar profesor")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_profesor()
        elif opcion == "2":
            listar_profesores()
        elif opcion == "3":
            editar_profesor()
        elif opcion == "4":
            eliminar_profesor()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

# GUI de profesores
def agregar_profesor_gui(nombre, apellido, dni, correo, direccion):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO profesor (nombre, apellido, dni, correo, direccion) VALUES (?, ?, ?, ?, ?)",
                   (nombre, apellido, dni, correo, direccion))
    conexion.commit()
    conexion.close()

def obtener_profesores():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, apellido, dni, correo, direccion FROM profesor")
    profesores = cursor.fetchall()
    conexion.close()
    return profesores

def eliminar_profesor_por_dni(dni):
    conexion = sqlite3.connect("ites_academico.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM profesor WHERE dni = ?", (dni,))
    profesor = cursor.fetchone()

    if not profesor:
        conexion.close()
        return False

    cursor.execute("DELETE FROM profesor WHERE dni = ?", (dni,))
    conexion.commit()
    conexion.close()
    return True