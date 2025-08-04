

from database.conexion import crear_tablas
import menu

if __name__ == "__main__":
    crear_tablas()
    menu.mostrar_menu()