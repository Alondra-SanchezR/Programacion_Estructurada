import os
from openpyxl import Workbook
from datetime import datetime
from clientes.cliente import obtener_clientes
from proyectos.proyecto import obtener_proyectos

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n\t\t ⏮️ Presiona Enter para continuar... ⏭️")

def menu_usuarios():
    print("\n\t🏗️ Sistema de Gestión de Proyectos Civiles 🏗️\n")
    print("\t1.- Registro")
    print("\t2.- Login")
    print("\t3.- Salir")
    return input("\n\tElige una opción: ").upper().strip()

def menu_principal():
    print("\n\t📁 Menú Principal\n")
    print("\t1.- Gestionar Clientes")
    print("\t2.- Gestionar Proyectos")
    print("\t3.- Exportar Clientes")      # Nueva opción
    print("\t4.- Exportar Proyectos")    # Nueva opción
    print("\t5.- Cerrar Sesión")         # Cambia el número de la opción de cerrar sesión
    return input("\n\tElige una opción: ").upper().strip()


def exportar_clientes(usuario_id):
    clientes = obtener_clientes(usuario_id)
    if not clientes:
        print("⚠️ No hay clientes para exportar.")
        return False

    wb = Workbook()
    ws = wb.active
    ws.title = "Clientes"

    # Encabezados
    ws.append(["ID", "Nombre", "Teléfono", "Dirección", "Correo"])

    # Datos
    for c in clientes:
        ws.append(list(c))

    nombre_archivo = f"clientes_{usuario_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    wb.save(nombre_archivo)
    print(f"✅ Clientes exportados a {nombre_archivo}")
    return True

def exportar_proyectos(cliente_id):
    proyectos = obtener_proyectos(cliente_id)
    if not proyectos:
        print("⚠️ No hay proyectos para exportar.")
        return False

    wb = Workbook()
    ws = wb.active
    ws.title = "Proyectos"

    # Encabezados
    ws.append(["ID", "Nombre", "Ubicación", "Presupuesto", "Materiales", "Tareas"])

    # Datos
    for p in proyectos:
        ws.append(list(p))

    nombre_archivo = f"proyectos_{cliente_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    wb.save(nombre_archivo)
    print(f"✅ Proyectos exportados a {nombre_archivo}")
    return True