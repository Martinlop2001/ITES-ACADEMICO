

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
    conn = sqlite3.connect('ites_academico.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profesor")
    profesores = cursor.fetchall()
    conn.close()
    return profesores

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

def eliminar_profesor(id_profesor):
    conn = sqlite3.connect('ites_academico.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM profesor WHERE id = ?", (id_profesor,))
    conn.commit()
    conn.close()



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

def eliminar_profesor_por_id(id_profesor):
    conn = sqlite3.connect("ites_academico.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM profesor WHERE id = ?", (id_profesor,))
    conn.commit()
    filas_afectadas = cursor.rowcount
    conn.close()
    return filas_afectadas > 0