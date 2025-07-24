from conexionBD import *
import datetime

def registrar(nombre,apellidos,email,contrasena):
    try:
        cursor.execute("INSERT INTO usuarios (nombre,apellidos,email,password,fecha) " \
        "values (%s,%s,%s,%s)",())
        conexion.commit()
        return True
    except:
        return False
    