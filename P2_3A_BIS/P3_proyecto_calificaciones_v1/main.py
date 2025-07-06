import calificaciones

def main():
    datos = []

    while True:
        calificaciones.borrarPantalla()
        opcion = calificaciones.menu_principal()

        if opcion == "1":
            calificaciones.agregar_calificacion(datos)
            calificaciones.esperarTecla()
        elif opcion == "2":
            calificaciones.mostrar_calificaciones(datos)
            calificaciones.esperarTecla()
        elif opcion == "3":
            calificaciones.calcular_promedio(datos)
            calificaciones.esperarTecla()
        elif opcion == "4":
            print("\n\t👋 Terminaste la ejecución del programa. ¡Gracias por usarlo!")
            calificaciones.borrarPantalla()
            break
        else:
            print("\n\t⚠️ Opción no válida, por favor selecciona una opción del menú (1-4)")
            calificaciones.esperarTecla()

if __name__ == "__main__":
    main()