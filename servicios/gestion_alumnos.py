

from database.conexion import conectar
from modelos.alumno import Alumno
from servicios.inscripciones import inscribir_alumno

def agregar_alumno():
    print("\n--- Agregar Alumno ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    correo = input("Correo: ")
    direccion = input("Dirección: ")

    alumno = Alumno(nombre, apellido, dni, correo, direccion)

    conexion = conectar()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            INSERT INTO alumno (nombre, apellido, dni, correo, direccion)
            VALUES (?, ?, ?, ?, ?)
        """, (alumno.nombre, alumno.apellido, alumno.dni, alumno.correo, alumno.direccion))
        conexion.commit()
        print("Alumno agregado correctamente.")
    except Exception as e:
        print("Error al agregar alumno:", e)
    finally:
        conexion.close()

def listar_alumnos():
    print("\n--- Lista de Alumnos ---")
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, apellido, dni, correo, direccion FROM alumno")
    alumnos = cursor.fetchall()

    if alumnos:
        for a in alumnos:
            print(f"[{a[0]}] {a[1]} {a[2]} - DNI: {a[3]} - Correo: {a[4]} - Dirección: {a[5]}")
    else:
        print("No hay alumnos registrados.")

    conexion.close()

def editar_alumno():
    listar_alumnos()
    alumno_id = input("Ingrese el ID del alumno a editar: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre, apellido, dni, correo, direccion FROM alumno WHERE id = ?", (alumno_id,))
    alumno = cursor.fetchone()

    if not alumno:
        print("Alumno no encontrado.")
        conexion.close()
        return

    print("Deje vacío para no modificar.")

    nombre = input(f"Nombre [{alumno[0]}]: ") or alumno[0]
    apellido = input(f"Apellido [{alumno[1]}]: ") or alumno[1]
    dni = input(f"DNI [{alumno[2]}]: ") or alumno[2]
    correo = input(f"Correo [{alumno[3]}]: ") or alumno[3]
    direccion = input(f"Dirección [{alumno[4]}]: ") or alumno[4]

    try:
        cursor.execute("""
            UPDATE alumno
            SET nombre = ?, apellido = ?, dni = ?, correo = ?, direccion = ?
            WHERE id = ?
        """, (nombre, apellido, dni, correo, direccion, alumno_id))
        conexion.commit()
        print("Alumno actualizado correctamente.")
    except Exception as e:
        print("Error al actualizar alumno:", e)
    finally:
        conexion.close()

def eliminar_alumno():
    listar_alumnos()
    alumno_id = input("Ingrese el ID del alumno a eliminar: ")

    confirmacion = input(f"¿Está seguro que desea eliminar al alumno con ID {alumno_id}? (s/n): ")
    if confirmacion.lower() != 's':
        print("Eliminación cancelada.")
        return

    conexion = conectar()
    cursor = conexion.cursor()

    try:
        cursor.execute("DELETE FROM alumno WHERE id = ?", (alumno_id,))
        conexion.commit()
        print("Alumno eliminado correctamente.")
    except Exception as e:
        print("Error al eliminar alumno:", e)
    finally:
        conexion.close()


def menu_interactivo():
    while True:
        print("\n--- Gestión de Alumnos ---")
        print("1. Agregar alumno")
        print("2. Listar alumnos")
        print("3. Editar alumno")
        print("4. Eliminar alumno")
        print("5. Inscribir alumno a una materia")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_alumno()
        elif opcion == "2":
            listar_alumnos()
        elif opcion == "3":
            editar_alumno()
        elif opcion == "4":
            eliminar_alumno()
        elif opcion == "5":
            inscribir_alumno()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
