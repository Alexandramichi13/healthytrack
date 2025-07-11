#db.py
import sqlite3
DB_NAME = "habitos.db"

def conectar():
    return sqlite3.connect(DB_NAME)

#PERSONAS
def agregar_persona(nombre, edad, genero):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Personas (nombre, edad, genero) VALUES (?, ?, ?)", (nombre, edad, genero))
    conn.commit()
    conn.close()

def obtener_personas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Personas")
    personas = cursor.fetchall()
    conn.close()
    return personas

def eliminar_persona(id_persona):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Personas WHERE id_persona = ?", (id_persona,))
    conn.commit()
    conn.close()

#HABITOS
def agregar_habito(nombre, tipo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Habitos (nombre, tipo) VALUES (?, ?)", (nombre, tipo))
    conn.commit()
    conn.close()

def obtener_habitos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Habitos")
    habitos = cursor.fetchall()
    conn.close()
    return habitos

def eliminar_habito(id_habito):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Habitos WHERE id_habito = ?", (id_habito,))
    conn.commit()
    conn.close()

#REGISTROS
def agregar_registro(fecha, id_persona, id_habito, cumplido):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO RegistrosDiarios (fecha, id_persona, id_habito, cumplido) VALUES (?, ?, ?, ?)", 
                   (fecha, id_persona, id_habito, cumplido))
    conn.commit()
    conn.close()

def obtener_registros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT r.id_registro, r.fecha, p.nombre, h.nombre, r.cumplido
        FROM RegistrosDiarios r
        JOIN Personas p ON r.id_persona = p.id_persona
        JOIN Habitos h ON r.id_habito = h.id_habito
    """)
    registros = cursor.fetchall()
    conn.close()
    return registros

