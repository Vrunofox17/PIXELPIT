import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('escuela.db')
cursor = conn.cursor()

# Crear tablas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS niveles_educativos (
        id_nivel INTEGER PRIMARY KEY,
        nombre_nivel TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grados (
        id_grado INTEGER PRIMARY KEY,
        nombre_grado TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS alumnos (
        id_alumno INTEGER PRIMARY KEY,
        nombre TEXT,
        apellido TEXT,
        fecha_nacimiento DATE,
        direccion TEXT,
        telefono TEXT,
        correo_electronico TEXT,
        nivel_educativo INTEGER,
        grado INTEGER,
        FOREIGN KEY (nivel_educativo) REFERENCES niveles_educativos(id_nivel),
        FOREIGN KEY (grado) REFERENCES grados(id_grado)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS inscripciones (
        id_inscripcion INTEGER PRIMARY KEY,
        id_alumno INTEGER,
        fecha_inscripcion DATE,
        año_academico INTEGER,
        FOREIGN KEY (id_alumno) REFERENCES alumnos(id_alumno)
    )
''')

# Insertar datos iniciales
cursor.execute("INSERT INTO niveles_educativos (nombre_nivel) VALUES ('Inicial/Jardín')")
cursor.execute("INSERT INTO niveles_educativos (nombre_nivel) VALUES ('Preescolar')")
cursor.execute("INSERT INTO niveles_educativos (nombre_nivel) VALUES ('Básica 1-9')")

cursor.execute("INSERT INTO grados (nombre_grado) VALUES ('Jardín')")
cursor.execute("INSERT INTO grados (nombre_grado) VALUES ('Preescolar')")
cursor.execute("INSERT INTO grados (nombre_grado) VALUES ('1')")
cursor.execute("INSERT INTO grados (nombre_grado) VALUES ('2')")
cursor.execute("INSERT INTO grados (nombre_grado) VALUES ('3')")
cursor.execute("INSERT INTO grados (nombre_grado) VALUES ('4')")
cursor.execute("INSERT INTO grados (nombre_grado) VALUES ('5')")
cursor.execute("INSERT INTO grados (nombre_grado) VALUES ('6')")
cursor.execute("INSERT INTO grados (nombre_grado) VALUES ('7')")
cursor.execute("INSERT INTO grados (nombre_grado) VALUES ('8')")
cursor.execute("INSERT INTO grados (nombre_grado) VALUES ('9')")

# Guardar cambios
conn.commit()

# Función para registrar un nuevo alumno
def registrar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (DD/MM/AAAA): ")
    direccion = input("Ingrese la dirección del alumno: ")
    telefono = input("Ingrese el teléfono del alumno: ")
    correo_electronico = input("Ingrese el correo electrónico del alumno: ")
    nivel_educativo = int(input("Ingrese el nivel educativo del alumno (1-3): "))
    grado = int(input("Ingrese el grado del alumno (1-9): "))

    cursor.execute("INSERT INTO alumnos (nombre, apellido, fecha_nacimiento, direccion, telefono, correo_electronico, nivel_educativo, grado) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                   (nombre, apellido, fecha_nacimiento, direccion, telefono, correo_electronico, nivel_educativo, grado))
    conn.commit()
    print("Alumno registrado con éxito.")

# Función para enviar datos a tu correo electrónico
import smtplib
from email.mime.text import MIMEText

def enviar_correo(alumno):
    correo_remitente = "tu_correo@gmail.com"
    contraseña = "tu_contraseña"
    correo_destinatario = "tu_correo@gmail.com"
    asunto = "Nuevo alumno registrado"
    cuerpo = f"Nombre: {alumno[1]}\nApellido: {alumno[2]}\nFecha de nacimiento: {alumno[3]}\nDirección: {alumno[4]}\nTeléfono: {alumno[5]}\nCorreo electrónico: {alumno[6]}\nNivel educativo: {alumno[7]}\nGrado: {alumno[8]}"

    msg = MIMEText(cuerpo)
    msg['Subject'] = asunto
    msg['From'] = correo_remit