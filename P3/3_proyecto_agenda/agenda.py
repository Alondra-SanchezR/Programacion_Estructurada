import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    import os
    os.system('cls')

def esperar_Tecla():
    input("\n" + "\t" * 4 + "🕹️  Presiona cualquier tecla para continuar... ")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_agenda"
        )
        return conexion
    except Error as e:
        print(f"\n❌ Error al conectar con la base de datos: {e}")
        return None

def menu_principal():
    borrarPantalla()
    print("\n" + "\t" * 3 + "📒═══════════════════════════════════════════════")
    print("\t" * 3 + "     SISTEMA DE GESTIÓN DE CONTACTOS     ")
    print("\t" * 3 + "═══════════════════════════════════════════════📒\n")
    print("\t" * 4 + "1️⃣  ➕ Agregar contacto")
    print("\t" * 4 + "2️⃣  📋 Mostrar todos los contactos")
    print("\t" * 4 + "3️⃣  🔍 Buscar contacto por nombre")
    print("\t" * 4 + "4️⃣  📝 Modificar contacto")
    print("\t" * 4 + "5️⃣  🗑️ Eliminar contacto")
    print("\t" * 4 + "6️⃣  ❌ Salir del programa\n")
    return input("\t" * 4 + "📌 Elige una opción (1-6): ")

def agregar_contacto():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        print("\n" + "\t" * 4 + "📝════════════ AGREGAR CONTACTO ════════════\n")
        nombre = input("\t" * 4 + "👤 Nombre del contacto: ").upper().strip()
        telefono = input("\t" * 4 + "📞 Teléfono: ").strip()
        email = input("\t" * 4 + "📧 Correo electrónico: ").lower().strip()

        cursor = conexionBD.cursor()
        sql = "INSERT INTO contactos (nombre, telefono, email) VALUES (%s, %s, %s)"
        val = (nombre, telefono, email)
        cursor.execute(sql, val)
        conexionBD.commit()

        print("\n" + "\t" * 4 + "✅ Contacto agregado con éxito.\n")
        esperar_Tecla()
    else:
        print("\n" + "\t" * 4 + "❌ No se pudo conectar a la base de datos.")

def mostrar_contactos():
    borrarPantalla()
    print("\n" + "\t" * 4 + "📋════════════ LISTADO DE CONTACTOS ════════════\n")
    conexionBD = conectar()
    if conexionBD:
        cursor = conexionBD.cursor()
        cursor.execute("SELECT * FROM contactos")
        registros = cursor.fetchall()

        if registros:
            print("\t" * 2 + f"{'🆔 ID':<5}{'👤 Nombre':<22}{'📞 Teléfono':<20}{'📧 Correo':<30}")
            print("\t" * 2 + "-" * 75)
            for fila in registros:
                print("\t" * 2 + f"{fila[0]:<5}{fila[1]:<22}{fila[2]:<20}{fila[3]:<30}")
            print("\t" * 2 + "-" * 75 + "\n")
        else:
            print("\n" + "\t" * 4 + "⚠️  No hay contactos registrados.\n")
        esperar_Tecla()
    else:
        print("\n" + "\t" * 4 + "❌ No se pudo conectar a la base de datos.")

def buscar_contacto():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        print("\n" + "\t" * 4 + "🔎════════════ BUSCAR CONTACTO ════════════\n")
        nombre = input("\t" * 4 + "👤 Nombre del contacto a buscar: ").upper().strip()

        cursor = conexionBD.cursor()
        sql = "SELECT * FROM contactos WHERE nombre = %s"
        cursor.execute(sql, (nombre,))
        registros = cursor.fetchall()

        if registros:
            print("\t" * 2 + f"{'🆔 ID':<5}{'👤 Nombre':<22}{'📞 Teléfono':<20}{'📧 Correo':<30}")
            print("\t" * 2 + "-" * 75)
            for fila in registros:
                print("\t" * 2 + f"{fila[0]:<5}{fila[1]:<22}{fila[2]:<20}{fila[3]:<30}")
            print("\t" * 2 + "-" * 75 + "\n")
            print("\t" * 4 + "✅ Contacto encontrado.")
        else:
            print("\n" + "\t" * 4 + "⚠️  El contacto no existe.")
        esperar_Tecla()
    else:
        print("\n" + "\t" * 4 + "❌ No se pudo conectar a la base de datos.")

def modificar_contacto():
    borrarPantalla()
    print("\n" + "\t" * 4 + "✏️════════════ MODIFICAR CONTACTO ════════════\n")
    conexionBD = conectar()
    if conexionBD:
        nombre = input("\t" * 4 + "👤 Nombre del contacto a buscar: ").upper().strip()

        cursor = conexionBD.cursor()
        sql = "SELECT * FROM contactos WHERE nombre = %s"
        cursor.execute(sql, (nombre,))
        registro = cursor.fetchone()

        if registro:
            print("\n" + "\t" * 4 + f"📄 Nombre: {registro[1]}")
            print("\t" * 4 + f"📞 Teléfono actual: {registro[2]}")
            print("\t" * 4 + f"📧 Email actual: {registro[3]}")
            respuesta = input("\n" + "\t" * 4 + "¿Deseas modificar este contacto? (si/no): ").lower().strip()

            if respuesta == "si":
                nuevo_tel = input("\t" * 4 + "📞 Nuevo teléfono: ").strip()
                nuevo_email = input("\t" * 4 + "📧 Nuevo correo electrónico: ").lower().strip()
                sql_update = "UPDATE contactos SET telefono = %s, email = %s WHERE nombre = %s"
                cursor.execute(sql_update, (nuevo_tel, nuevo_email, nombre))
                conexionBD.commit()
                print("\n" + "\t" * 4 + "✅ Contacto modificado exitosamente.\n")
            else:
                print("\n" + "\t" * 4 + "🚫 Modificación cancelada.\n")
        else:
            print("\n" + "\t" * 4 + "⚠️  El contacto no existe.")
        conexionBD.close()
        esperar_Tecla()
    else:
        print("\n" + "\t" * 4 + "❌ No se pudo conectar a la base de datos.")

def eliminar_contacto():
    borrarPantalla()
    print("\n" + "\t" * 4 + "🗑️════════════ ELIMINAR CONTACTO ════════════\n")
    conexionBD = conectar()
    if conexionBD:
        nombre = input("\t" * 4 + "👤 Nombre del contacto a eliminar: ").upper().strip()

        cursor = conexionBD.cursor()
        sql = "SELECT * FROM contactos WHERE nombre = %s"
        cursor.execute(sql, (nombre,))
        registro = cursor.fetchone()

        if registro:
            confirmar = input(f"\n\t\t\t\t👉 ¿Estás seguro de eliminar el contacto {nombre}? (si/no): ").lower().strip()
            if confirmar == "si":
                cursor.execute("DELETE FROM contactos WHERE nombre = %s", (nombre,))
                conexionBD.commit()
                print("\n" + "\t" * 4 + "✅ Contacto eliminado correctamente.\n")
            else:
                print("\n" + "\t" * 4 + "🚫 Eliminación cancelada.\n")
        else:
            print("\n" + "\t" * 4 + "⚠️  El contacto no existe.")
        conexionBD.close()
        esperar_Tecla()
    else:
        print("\n" + "\t" * 4 + "❌ No se pudo conectar a la base de datos.")
