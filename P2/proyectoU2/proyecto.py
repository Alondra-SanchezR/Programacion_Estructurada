import os
import shutil

# ═════════════════════════════════════════════════════════════
#     🏗️ Sistema de Gestión para Ingeniero Civil 🏗️
#     Programación Estructurada con Listas y Diccionarios
# ═════════════════════════════════════════════════════════════


def clear_screen():
    #Limpia la pantalla de la consola.
    os.system('cls' if os.name == 'nt' else 'clear')


def print_center(text):
    #Imprime texto centrado según el ancho de la terminal.
    width = shutil.get_terminal_size((80, 20)).columns
    print(text.center(width))


def esperar_tecla():
    #Pausa la ejecución esperando que el usuario presione Enter.
    input("\n\t\t\t ⏮️  Presiona Enter para continuar... ⏭️")

def mostrar_menu():
    print("\n")
    print_center("🏗️ ═══ Sistema de Gestión para Ingeniero Civil ═══ 🏗️")
    print("\n")
    opciones = [
        "1. ➕  Agregar Proyecto",
        "2. 📋  Ver Todos los Proyectos",
        "3. 📝  Actualizar Proyecto",
        "4. 🗑️  Eliminar Proyecto",
        "5. 🚪  Salir"
    ]
    
    for opt in opciones:
        print_center(opt)
    print("\n")
    elección = input_center = "Seleccione una opción (1-5): "
    return input(input_center).strip()


def agregar_proyecto(proyectos):
    print("\n")
    print_center("📌 ── Agregar Proyecto ──")
    id_proyecto = input("\nID del Proyecto: ").strip()
   
    if not id_proyecto:
        print_center("⚠️ El ID no puede estar vacío.")
        return
    if id_proyecto in proyectos:
        print_center("❌ ¡El ID del proyecto ya existe!")
        return
    nombre = input("Nombre del Proyecto: ").strip()
    ubicacion = input("Ubicación del Proyecto: ").strip()

    # Validación de presupuesto
    while True:
        try:
            presupuesto = float(input("Presupuesto del Proyecto: ").strip())
            if presupuesto < 0:
                raise ValueError("Presupuesto negativo")
            break
        except ValueError:
            print_center(" ❗ Presupuesto inválido. Ingresa un número positivo.")

    materiales = input("Materiales (separados por comas): ").split(",")
    tareas = input("Tareas (separadas por comas): ").split(",")

    proyectos[id_proyecto] = {
        "nombre": nombre,
        "ubicacion": ubicacion,
        "presupuesto": presupuesto,
        "materiales": [m.strip() for m in materiales if m.strip()],
        "tareas": [t.strip() for t in tareas if t.strip()]
    }
    print("\n")
    print_center(f"✅ Proyecto '{nombre}' agregado exitosamente!")

def ver_proyectos(proyectos):
    print("\n")
    print_center("📂 ── Lista de Proyectos ──")
    if not proyectos:
        print_center("📭 No hay proyectos disponibles.")
        return
    for pid, det in proyectos.items():
        print("\n" + "─" * 80)
        print_center(f"🔖 ID: {pid} | 📌 Nombre: {det['nombre']}")
        print_center(f"📍 Ubicación: {det['ubicacion']} | 💵 Presupuesto: ${det['presupuesto']:.2f}")
        print_center(f"🧱 Materiales: {', '.join(det['materiales'])}")
        print_center(f"🧰 Tareas: {', '.join(det['tareas'])}")
        print("─" * 80)


def actualizar_proyecto(proyectos):
    print("\n")
    print_center("🛠️ ── Actualizar Proyecto ──")
    
    pid = input("ID del Proyecto a actualizar: ").strip()
    if pid not in proyectos:
        print_center("❌ ¡Proyecto no encontrado!")
        return
    actual = proyectos[pid]
    print_center("🔄 Deja vacío para mantener el valor actual.")
    nombre = input(f"Nombre ({actual['nombre']}): ").strip() or actual['nombre']
    ubicacion = input(f"Ubicación ({actual['ubicacion']}): ").strip() or actual['ubicacion']

    presupuesto_in = input(f"Presupuesto ({actual['presupuesto']}): ").strip()
    if presupuesto_in:
        try:
            presupuesto = float(presupuesto_in)
        except ValueError:
            presupuesto = actual['presupuesto']
            print_center("⚠️ Valor inválido. Presupuesto anterior conservado.")
    else:
        presupuesto = actual['presupuesto']

    mats = input(f"Materiales (actuales: {', '.join(actual['materiales'])}): ")
    materiales = [m.strip() for m in mats.split(",")] if mats else actual['materiales']
    tas = input(f"Tareas (actuales: {', '.join(actual['tareas'])}): ")
    tareas = [t.strip() for t in tas.split(",")] if tas else actual['tareas']

    proyectos[pid] = {
        "nombre": nombre,
        "ubicacion": ubicacion,
        "presupuesto": presupuesto,
        "materiales": materiales,
        "tareas": tareas
    }
    print("\n")
    print_center(f"✅ Proyecto '{pid}' actualizado exitosamente!")

def eliminar_proyecto(proyectos):
    print("\n")
    print_center("❌ ── Eliminar Proyecto ──")
    
    pid = input("ID del Proyecto a eliminar: ").strip()
    if pid in proyectos:
        del proyectos[pid]
        print_center(f"🗑️ Proyecto '{pid}' eliminado exitosamente!")
    else:
        print_center("⚠️ ¡Proyecto no encontrado!")