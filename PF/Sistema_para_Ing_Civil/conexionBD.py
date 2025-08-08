import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_civil"
    )
    cursor = conexion.cursor(buffered=True)
except:
    print("⚠️ Error: No se pudo conectar a la base de datos.")
