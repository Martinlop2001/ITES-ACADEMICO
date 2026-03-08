



import psycopg2

def conectar():

    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="ites_academico",
        user="postgres",
        password="3239"
    )

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profesor (
        id SERIAL PRIMARY KEY,
        dni VARCHAR(50) UNIQUE,
        nombre VARCHAR(100),
        apellido VARCHAR(100),
        correo VARCHAR(150)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alumno (
        id SERIAL PRIMARY KEY,
        dni VARCHAR(50) UNIQUE,
        nombre VARCHAR(100),
        apellido VARCHAR(100),
        correo VARCHAR(150)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS materia (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(150) NOT NULL,
        profesor_id INTEGER NOT NULL,
        FOREIGN KEY (profesor_id) REFERENCES profesor(id) ON DELETE CASCADE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS falta (
        id SERIAL PRIMARY KEY,
        alumno_id INTEGER,
        profesor_id INTEGER,
        materia_id INTEGER,
        fecha TEXT,
        motivo TEXT,
        FOREIGN KEY (alumno_id) REFERENCES alumno(id) ON DELETE CASCADE,
        FOREIGN KEY (profesor_id) REFERENCES profesor(id) ON DELETE CASCADE,
        FOREIGN KEY (materia_id) REFERENCES materia(id) ON DELETE CASCADE
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL,
        password TEXT NOT NULL,
        rol VARCHAR(50) NOT NULL,
        referencia_id INTEGER
    )
    """)

    conexion.commit()
    conexion.close()