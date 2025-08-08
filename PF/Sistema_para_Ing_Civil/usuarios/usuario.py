from conexionBD import conexion, cursor
import hashlib
import datetime

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def registrar(nombre, apellidos, email, password):
    try:
        fecha = datetime.datetime.now()
        hashed = hash_password(password)
        cursor.execute("""
            INSERT INTO usuarios (nombre, apellidos, email, password, fecha)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, apellidos, email, hashed, fecha))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return False

def inicio_sesion(email, password):
    try:
        hashed = hash_password(password)
        cursor.execute("SELECT * FROM usuarios WHERE email=%s AND password=%s", (email, hashed))
        return cursor.fetchone()
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")
        return None
