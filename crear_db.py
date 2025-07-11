import sqlite3

#Conexión a la base de datos 
conn = sqlite3.connect("habitos.db")
cursor = conn.cursor()

#Crear tabla Personas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Personas (
    id_persona INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER,
    genero TEXT
)
""")

#Crear tabla Habitos
cursor.execute("""
CREATE TABLE IF NOT EXISTS Habitos (
    id_habito INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT
)
""")

#Crear tabla RegistrosDiarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS RegistrosDiarios (
    id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    id_persona INTEGER,
    id_habito INTEGER,
    cumplido BOOLEAN,
    FOREIGN KEY (id_persona) REFERENCES Personas(id_persona),
    FOREIGN KEY (id_habito) REFERENCES Habitos(id_habito)
)
""")

#Confirmar y cerrar
conn.commit()
conn.close()

print("¡Base de datos 'habitos.db' creada correctamente con las 3 tablas!")
