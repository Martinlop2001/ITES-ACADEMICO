

from database.conexion import conectar
from modelos.materia import Materia

def agregar_materia():
    print("\n--- Agregar Materia ---")
    nombre = input("Nombre de la materia: ")

    # Mostrar profesores disponibles
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, apellido FROM profesor")
    profesores = cursor.fetchall()

    if not profesores:
        print("No hay profesores registrados. Agregue uno primero.")
        conexion.close()
        return

    print("\nProfesores disponibles:")
    for p in profesores:
        print(f"{p[0]}: {p[1]} {p[2]}")

    profesor_id = input("Ingrese el ID del profesor que dicta la materia: ")

    materia = Materia(nombre, profesor_id)

    try:
        cursor.execute("""
            INSERT INTO materia (nombre, profesor_id)
            VALUES (?, ?)
        """, (materia.nombre, materia.profesor_id))
        conexion.commit()
        print("Materia agregada correctamente.")
    except Exception as e:
        print("Error al agregar materia:", e)
    finally:
        conexion.close()

def listar_materias():
    print("\n--- Lista de Materias ---")
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT m.id, m.nombre, p.nombre, p.apellido
        FROM materia m
        LEFT JOIN profesor p ON m.profesor_id = p.id
    """)
    materias = cursor.fetchall()

    if materias:
        for m in materias:
            print(f"[{m[0]}] {m[1]} - Profesor: {m[2]} {m[3]}")
    else:
        print("No hay materias registradas.")

    conexion.close()

def editar_materia():
    listar_materias()
    materia_id = input("Ingrese el ID de la materia a editar: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre, profesor_id FROM materia WHERE id = ?", (materia_id,))
    materia = cursor.fetchone()

    if not materia:
        print("Materia no encontrada.")
        conexion.close()
        return

    print("Deje vacío para no modificar.")

    nombre = input(f"Nombre [{materia[0]}]: ") or materia[0]

    cursor.execute("SELECT id, nombre, apellido FROM profesor")
    profesores = cursor.fetchall()

    print("\nProfesores disponibles:")
    for p in profesores:
        print(f"{p[0]}: {p[1]} {p[2]}")

    profesor_id = input(f"ID del profesor [{materia[1]}]: ") or materia[1]

    try:
        cursor.execute("""
            UPDATE materia
            SET nombre = ?, profesor_id = ?
            WHERE id = ?
        """, (nombre, profesor_id, materia_id))
        conexion.commit()
        print("Materia actualizada correctamente.")
    except Exception as e:
        print("Error al actualizar materia:", e)
    finally:
        conexion.close()

def eliminar_materia():
    listar_materias()
    materia_id = input("Ingrese el ID de la materia a eliminar: ")

    confirmacion = input(f"¿Está seguro que desea eliminar la materia con ID {materia_id}? (s/n): ")
    if confirmacion.lower() != 's':
        print("Eliminación cancelada.")
        return

    conexion = conectar()
    cursor = conexion.cursor()

    try:
        cursor.execute("DELETE FROM materia WHERE id = ?", (materia_id,))
        conexion.commit()
        print("Materia eliminada correctamente.")
    except Exception as e:
        print("Error al eliminar materia:", e)
    finally:
        conexion.close()



def menu_interactivo():
    while True:
        print("\n--- Gestión de Materias ---")
        print("1. Agregar materia")
        print("2. Listar materias")
        print("3. Editar materia")
        print("4. Eliminar materia")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_materia()
        elif opcion == "2":
            listar_materias()
        elif opcion == "3":
            editar_materia()
        elif opcion == "4":
            eliminar_materia()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")