import funciones
from usuarios import usuario
from clientes import cliente
from proyectos import proyecto
from getpass import getpass

def main():
    usuario_actual = None
    while True:
        funciones.borrarPantalla()
        opcion = funciones.menu_usuarios()

        if opcion == "1" or opcion.upper() == "REGISTRO":
            funciones.borrarPantalla()
            print("\n\t..:: Registro de Usuario ::..")
            nombre = input("Nombre: ").strip().upper()
            apellidos = input("Apellidos: ").strip().upper()
            email = input("Email: ").strip().lower()
            password = getpass("Contraseña: ").strip()
            if usuario.registrar(nombre, apellidos, email, password):
                print("\n✅ Usuario registrado correctamente.")
            else:
                print("\n❌ No se pudo registrar el usuario.")
            funciones.esperarTecla()

        elif opcion == "2" or opcion.upper() == "LOGIN":
            funciones.borrarPantalla()
            print("\n\t..:: Inicio de Sesión ::..")
            email = input("Email: ").strip().lower()
            password = getpass("Contraseña: ").strip()
            user = usuario.inicio_sesion(email, password)
            if user:
                usuario_actual = user
                print(f"\n✅ Bienvenido {user[1]} {user[2]}")
                funciones.esperarTecla()
                menu_principal(usuario_actual)
            else:
                print("\n❌ Email o contraseña incorrectos.")
                funciones.esperarTecla()

        elif opcion == "3" or opcion.upper() == "SALIR":
            print("\n🚪 Saliendo del sistema...")
            break

        else:
            print("\n⚠️ Opción no válida.")
            funciones.esperarTecla()

def menu_principal(usuario):
    while True:
        funciones.borrarPantalla()
        opcion = funciones.menu_principal()

        if opcion == "1":
            gestionar_clientes(usuario[0])  # usuario_id

        elif opcion == "2":
            gestionar_proyectos(usuario[0])  # usuario_id

        elif opcion == "3":
            funciones.exportar_clientes(usuario[0])
            funciones.esperarTecla()

        elif opcion == "4":
            cliente_id = input("ID del cliente para exportar sus proyectos: ")
            funciones.exportar_proyectos(cliente_id)
            funciones.esperarTecla()

        elif opcion == "5":
            print("\n👋 Cerrando sesión...")
            break

        else:
            print("\n⚠️ Opción inválida.")
            funciones.esperarTecla()

def gestionar_clientes(usuario_id):
    while True:
        funciones.borrarPantalla()
        print("\n\t👤 Gestión de Clientes\n")
        print("1. Agregar Cliente")
        print("2. Ver Clientes")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver")
        op = input("\nElige una opción: ").strip()

        if op == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            correo = input("Correo: ")
            if cliente.agregar_cliente(nombre, telefono, direccion, correo, usuario_id):
                print("✅ Cliente agregado.")
            else:
                print("❌ No se pudo agregar.")
            funciones.esperarTecla()

        elif op == "2":
            clientes_usuario = cliente.obtener_clientes(usuario_id)
            if not clientes_usuario:
                print("📭 No hay clientes.")
            else:
                for c in clientes_usuario:
                    print(f"\n🆔 ID: {c[0]}\n👤 Nombre: {c[1]}\n📞 Tel: {c[2]}\n🏠 Dirección: {c[3]}\n📧 Correo: {c[4]}")
            funciones.esperarTecla()

        elif op == "3":
            idc = input("ID del cliente a actualizar: ")
            nombre = input("Nuevo nombre: ")
            telefono = input("Nuevo teléfono: ")
            direccion = input("Nueva dirección: ")
            correo = input("Nuevo correo: ")
            if cliente.actualizar_cliente(idc, nombre, telefono, direccion, correo):
                print("✅ Cliente actualizado.")
            else:
                print("❌ Error al actualizar.")
            funciones.esperarTecla()

        elif op == "4":
            idc = input("ID del cliente a eliminar: ")
            if cliente.eliminar_cliente(idc):
                print("✅ Cliente eliminado.")
            else:
                print("❌ Error al eliminar.")
            funciones.esperarTecla()

        elif op == "5":
            break

        else:
            print("⚠️ Opción inválida.")
            funciones.esperarTecla()

def gestionar_proyectos(usuario_id):
    while True:
        funciones.borrarPantalla()
        print("\n\t📁 Gestión de Proyectos\n")
        print("1. Crear Proyecto")
        print("2. Ver Proyectos por Cliente")
        print("3. Actualizar Proyecto")
        print("4. Eliminar Proyecto")
        print("5. Volver")
        op = input("\nElige una opción: ").strip()

        if op == "1":
            nombre = input("Nombre del proyecto: ")
            ubicacion = input("Ubicación: ")
            presupuesto = input("Presupuesto: ")
            materiales = input("Materiales (separados por coma): ").split(",")
            tareas = input("Tareas (separadas por coma): ").split(",")
            cliente_id = input("ID del cliente asociado: ")
            if proyecto.agregar_proyecto(nombre, ubicacion, presupuesto, materiales, tareas, cliente_id):
                print("✅ Proyecto creado.")
            else:
                print("❌ No se pudo crear el proyecto.")
            funciones.esperarTecla()

        elif op == "2":
            cliente_id = input("ID del cliente para ver sus proyectos: ")
            proyectos_cliente = proyecto.obtener_proyectos(cliente_id)
            if not proyectos_cliente:
                print("📭 No hay proyectos para este cliente.")
            else:
                for p in proyectos_cliente:
                    print(f"""
🆔 ID: {p[0]}
📁 Nombre: {p[1]}
📍 Ubicación: {p[2]}
💵 Presupuesto: {p[3]}
🧱 Materiales: {p[4]}
📋 Tareas: {p[5]}
""")
            funciones.esperarTecla()

        elif op == "3":
            pid = input("ID del proyecto a actualizar: ")
            nombre = input("Nuevo nombre: ")
            ubicacion = input("Nueva ubicación: ")
            presupuesto = input("Nuevo presupuesto: ")
            materiales = input("Nuevos materiales (separados por coma): ").split(",")
            tareas = input("Nuevas tareas (separadas por coma): ").split(",")
            if proyecto.actualizar_proyecto(pid, nombre, ubicacion, presupuesto, materiales, tareas):
                print("✅ Proyecto actualizado.")
            else:
                print("❌ Error al actualizar.")
            funciones.esperarTecla()

        elif op == "4":
            pid = input("ID del proyecto a eliminar: ")
            if proyecto.eliminar_proyecto(pid):
                print("✅ Proyecto eliminado.")
            else:
                print("❌ Error al eliminar.")
            funciones.esperarTecla()

        elif op == "5":
            break

        else:
            print("⚠️ Opción inválida.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()

