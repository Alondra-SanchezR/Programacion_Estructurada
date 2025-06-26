'''
Crear un proyecto que permita gestionar (administrar) peliculas
Colocar un menú de opciones para agregar, borrar, modificara
mostrar, buscar, limpiar una lista de peliculas

notas:
1.-Utilizar funciones y mandar llamar desde otro 
archivo (modelo)
2.-Utilizar listas par almacenar los nombres de peliculas
'''

import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t .:::Gestion de peliculas::: \n\n\t "
    "¨1.-Agregar \n\n\t 2.-Borrar \n\t 3.-Modificar \n\t 4.-Mostrar \n\t"
    "5.-buscar \n\t 6.-Limpiar \n\t 7.-Salir")
    opcion=input("\n\n\t Elige una opción: ").upper()

    match opcion:
        case"1":
            peliculas.agregarPeliculas()
            peliculas.espereTecla()
        case"2":
            peliculas.borrarPeliculas()
            peliculas.espereTecla()
        case"3":
            peliculas.modificarPeliculas()
            peliculas.espereTecla()
        case"4":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
        case"5":
            peliculas.buscarPeliculas()
            peliculas.espereTecla()
        case"6":
            peliculas.limpiarPeliculas()
            peliculas.espereTecla()
        case"7":
           opcion=False
           print("\n\t Terminaste la ejecución del sistema. Gracias")
        case    _:
            opcion=True

            print("\n\t Opción invalida vuelva a intentar")