

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
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni TEXT UNIQUE,
        nombre TEXT,
        apellido TEXT,
        correo TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS materia (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        profesor_id INTEGER NOT NULL,
        FOREIGN KEY (profesor_id) REFERENCES profesor(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS falta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        alumno_id INTEGER,
        profesor_id INTEGER,
        materia_id INTEGER,
        fecha TEXT,
        motivo TEXT,
        FOREIGN KEY (alumno_id) REFERENCES alumno(id),
        FOREIGN KEY (profesor_id) REFERENCES profesor(id),
        FOREIGN KEY (materia_id) REFERENCES materia(id)
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    rol TEXT NOT NULL,
    referencia_id INTEGER
    )
    """)

    
    conexion.commit()
    conexion.close()