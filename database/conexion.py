

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'datos', 'ites_academico.db')

def conectar():
    conexion = sqlite3.connect("ites_academico.db")
    return sqlite3.connect(DB_PATH)
    return conexion

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profesor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            dni TEXT UNIQUE NOT NULL,
            correo TEXT,
            direccion TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alumno (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            dni TEXT UNIQUE NOT NULL,
            correo TEXT,
            direccion TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS materia (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            profesor_id INTEGER,
            FOREIGN KEY (profesor_id) REFERENCES profesor(id)
        )
    ''')

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS falta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            profesor_id INTEGER,
            fecha TEXT NOT NULL,
            motivo TEXT,
            FOREIGN KEY (profesor_id) REFERENCES profesor(id)
        )
    """)


    conexion.commit()
    conexion.close()