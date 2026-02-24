

import sqlite3

def conectar():
    return sqlite3.connect("ites_academico.db")

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profesor (
        id INTEGER PRIMARY KEY,
        dni TEXT UNIQUE,
        nombre TEXT,
        apellido TEXT,
        correo TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alumno (
        id INTEGER PRIMARY KEY,
        dni TEXT UNIQUE,
        nombre TEXT,
        apellido TEXT,
        correo TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS materia (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        profesor_id INTEGER,
        FOREIGN KEY (profesor_id) REFERENCES profesor(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS falta (
        id INTEGER PRIMARY KEY,
        materia_id INTEGER,
        fecha TEXT,
        motivo TEXT,
        FOREIGN KEY (materia_id) REFERENCES materia(id)
    )
    """)

    conexion.commit()
    conexion.close()