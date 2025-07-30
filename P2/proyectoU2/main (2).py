import os
import proyecto

def menu():
    proyectos_dict = {}
    while True:
        opcion = proyecto.mostrar_menu()
        if opcion == "1":
            proyecto.agregar_proyecto(proyectos_dict)
            proyecto.esperar_tecla()
        elif opcion == "2":
            proyecto.ver_proyectos(proyectos_dict)
            proyecto.esperar_tecla()
        elif opcion == "3":
            proyecto.actualizar_proyecto(proyectos_dict)
            proyecto.esperar_tecla()
        elif opcion == "4":
            proyecto.eliminar_proyecto(proyectos_dict)
            proyecto.esperar_tecla()
        elif opcion == "5":
            proyecto.print_center("¡Saliendo del sistema. Adiós!")
            break
        else:
            proyecto.print_center("Opción inválida, intenta de nuevo.")
            proyecto.esperar_tecla()

if __name__ == "__main__":
    menu()