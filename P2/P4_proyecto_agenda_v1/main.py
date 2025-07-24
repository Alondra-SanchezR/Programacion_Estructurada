import agenda

def main():
    agenda_contactos = {}
    opcion=True

    while opcion:
        agenda.borrarPantalla()
        opcion = agenda.menu_principal()

        if opcion == "1":
            agenda.agregar_contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "2":
            agenda.mostrar_contactos(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "3":
            agenda.buscar_contactos(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "4":
            agenda.modificar_contactos(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "5":
            agenda.eliminar_contactos(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "6":
            agenda.borrarPantalla()
            print("\n\t👋 Terminaste la ejecución del programa. ¡Gracias por usarlo!")
            opcion = False
        else:
            opcion = True
            print("\n\t⚠️ Opción no válida, por favor selecciona una opción del menú (1-4)")
            agenda.esperarTecla()

if __name__ == "__main__":
    main()