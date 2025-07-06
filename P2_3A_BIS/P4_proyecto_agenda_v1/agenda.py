def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\n\t\t\t\t🔸 Pulsa cualquier tecla para continuar... ")

# ───────────── Menú Principal ─────────────
def menu_principal():
    print("\n\t\t📇🌟 .::: SISTEMA DE GESTIÓN DE AGENDA DE CONTACTOS :::. 🌟📇\n")
    print("\t\t\t\t ➊ ➕ Añadir nuevo contacto")
    print("\t\t\t\t ➋ 📂 Ver lista de contactos")
    print("\t\t\t\t ➌ 🔍 Buscar contacto por nombre")
    print("\t\t\t\t ➍ ✏️ Modificar contacto")
    print("\t\t\t\t ➎ ❌ Eliminar contacto")
    print("\t\t\t\t ➏ 🚪 Salir del sistema\n")
    opcion = input("\t\t\t\t🔸 Selecciona una opción (1-6): ")
    return opcion

# ───────────── Agregar contacto ─────────────
def agregar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t➕ Añadir nuevo contacto\n")
    nombre = input("📛 Nombre: ").upper().strip()
    if nombre in agenda:
        print("\n⚠️ Este contacto ya existe.")
    else:
        tel = input("📞 Teléfono: ").strip()
        email = input("📧 E-mail: ").lower().strip()
        agenda[nombre] = [tel, email]
        print("\n✅ Contacto agregado con éxito.")

# ───────────── Mostrar contactos ─────────────
def mostrar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t📂 Lista de contactos\n")
    if not agenda:
        print("⚠️ No hay contactos en la agenda.")
    else:
        print(f"{'📛 Nombre':<20} {'📞 Teléfono':<20} {'📧 E-mail':<30}")
        print("-" * 70)
        for nombre, datos in agenda.items():
            print(f"{nombre:<20} {datos[0]:<20} {datos[1]:<30}")
        print("-" * 70)

# ───────────── Buscar contacto ─────────────
def buscar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t🔍 Buscar contacto\n")
    if not agenda:
        print("⚠️ No hay contactos en la agenda.")
    else:
        nombre = input("🔎 Nombre a buscar: ").upper().strip()
        if nombre in agenda:
            print(f"\n{'📛 Nombre':<20} {'📞 Teléfono':<20} {'📧 E-mail':<30}")
            print("-" * 70)
            print(f"{nombre:<20} {agenda[nombre][0]:<20} {agenda[nombre][1]:<30}")
            print("-" * 70)
        else:
            print("❌ Este contacto no existe.")

# ───────────── Modificar contacto ─────────────
def modificar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t✏️ Modificar contacto\n")
    if not agenda:
        print("⚠️ No hay contactos en la agenda.")
    else:
        nombre = input("✏️ Nombre del contacto: ").upper().strip()
        if nombre in agenda:
            print("\n📋 Valores actuales:")
            print(f"📛 Nombre: {nombre}")
            print(f"📞 Teléfono: {agenda[nombre][0]}")
            print(f"📧 E-mail: {agenda[nombre][1]}")
            resp = input("\n❓ ¿Deseas modificar este contacto? (si/no): ").lower().strip()
            if resp == "si":
                tel = input("📞 Nuevo Teléfono: ").strip()
                email = input("📧 Nuevo E-mail: ").lower().strip()
                agenda[nombre] = [tel, email]
                print("\n✅ Contacto modificado con éxito.")
        else:
            print("❌ Este contacto no existe.")

# ───────────── Eliminar contacto ─────────────
def eliminar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t❌ Eliminar contacto\n")
    if not agenda:
        print("⚠️ No hay contactos en la agenda.")
    else:
        nombre = input("🗑️ Nombre del contacto: ").upper().strip()
        if nombre in agenda:
            print("\n📋 Valores actuales:")
            print(f"📛 Nombre: {nombre}")
            print(f"📞 Teléfono: {agenda[nombre][0]}")
            print(f"📧 E-mail: {agenda[nombre][1]}")
            resp = input("\n❓ ¿Deseas eliminar este contacto? (si/no): ").lower().strip()
            if resp == "si":
                agenda.pop(nombre)
                print("\n✅ Contacto eliminado con éxito.")
        else:
            print("❌ Este contacto no existe.")