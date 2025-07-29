import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\n" + "\t" * 4 + "⏳ Pulsa cualquier tecla para continuar... ")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"⚠️ Error de conexión: {e}")
        return None

def menu_principal():
    print("\n" + "\t" * 3 + "🧮═══════════════════════════════════════════════")
    print("\t" * 3 + "         SISTEMA DE CALIFICACIONES          ")
    print("\t" * 3 + "═══════════════════════════════════════════════🧮\n")
    print("\t" * 4 + "1️⃣  ➕ Agregar alumno")
    print("\t" * 4 + "2️⃣  📄 Mostrar alumnos")
    print("\t" * 4 + "3️⃣  📊 Calcular promedios")
    print("\t" * 4 + "4️⃣  🔍 Buscar alumno")
    print("\t" * 4 + "5️⃣  ❌ Salir\n")
    return input("\t" * 4 + "📌 Elige una opción (1-5): ")

def agregarAlumno():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        print("\n" + "\t" * 4 + "🧾════════════ AGREGAR ALUMNO ════════════\n")
        nombre = input("\t" * 4 + "👤 Nombre del alumno: ").upper().strip()
        
        calificaciones = []
        for i in range(1, 4):
            while True:
                try:
                    cal = float(input(f"\t" * 4 + f"✏️  Ingrese calificación {i}: "))
                    if 0 <= cal <= 10:
                        calificaciones.append(cal)
                        break
                    else:
                        print("\t" * 4 + "🚫 Calificación fuera de rango (0-10).")
                except ValueError:
                    print("\t" * 4 + "🚫 Ingresa un número válido.")

        cursor = conexionBD.cursor()
        sql = "INSERT INTO alumnos (nombre, calif1, calif2, calif3) VALUES (%s, %s, %s, %s)"
        val = (nombre, calificaciones[0], calificaciones[1], calificaciones[2])
        cursor.execute(sql, val)
        conexionBD.commit()

        print("\n" + "\t" * 4 + "✅ ¡Alumno registrado con éxito!\n")
        esperarTecla()

def mostrarAlumnos():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        cursor = conexionBD.cursor()
        cursor.execute("SELECT * FROM alumnos")
        registros = cursor.fetchall()
        
        print("\n" + "\t" * 4 + "📚══════════ LISTA DE ALUMNOS ══════════📚\n")
        if registros:
            print("\t" * 2 + f"{'🆔 ID':<10}{'👨‍🎓 Nombre':<30}{'📘 Calif1':<10}{'📗 Calif2':<10}{'📕 Calif3':<10}")
            print("\t" * 2 + "-" * 70)
            for fila in registros:
                print("\t" * 2 + f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}")
            print("\t" * 2 + "-" * 70 + "\n")
        else:
            print("\t" * 4 + "⚠️  No hay alumnos registrados.\n")
        esperarTecla()

def calcularPromedios():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        cursor = conexionBD.cursor()
        cursor.execute("SELECT nombre, calif1, calif2, calif3 FROM alumnos")
        registros = cursor.fetchall()
        
        print("\n" + "\t" * 4 + "📈══════════ PROMEDIOS POR ALUMNO ══════════\n")
        if registros:
            total = 0
            print("\t" * 2 + f"{'👤 Nombre':<30}{'🎯 Promedio':<10}")
            print("\t" * 2 + "-" * 40)
            for fila in registros:
                promedio = (fila[1] + fila[2] + fila[3]) / 3
                total += promedio
                print("\t" * 2 + f"{fila[0]:<30}{promedio:<10.2f}")
            promedio_grupal = total / len(registros)
            print("\t" * 2 + "-" * 40)
            print(f"\n" + "\t" * 4 + f"🏆 Promedio grupal del grupo: {promedio_grupal:.2f}\n")
        else:
            print("\t" * 4 + "⚠️  No hay alumnos para calcular promedios.\n")
        conexionBD.close()
        esperarTecla()

def buscarAlumno():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        print("\n" + "\t" * 4 + "🔎════════════ BUSCAR ALUMNO ════════════\n")
        nombre = input("\t" * 4 + "🔤 Nombre del alumno a buscar: ").upper().strip()
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM alumnos WHERE nombre = %s"
        cursor.execute(sql, (nombre,))
        registro = cursor.fetchone()
        if registro:
            print(f"\n\t🆔 ID: {registro[0]}")
            print(f"\t👨‍🎓 Nombre: {registro[1]}")
            print(f"\t📘 Calif1: {registro[2]}")
            print(f"\t📗 Calif2: {registro[3]}")
            print(f"\t📕 Calif3: {registro[4]}\n")
        else:
            print("\t⚠️  Alumno no encontrado.\n")
        esperarTecla()
