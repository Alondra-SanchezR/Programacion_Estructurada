'''
Crear un proyecto que permita gestionar (administra) peliculas Colocar un menu de opciones: Agregar, Borrar, 
Modificar, Mostrar, Buscar, Limpiar una lista de peliculas.

Notas:
1.- Utilizar funciones y mandar llamar desde el archivo (modulo)
2.- Utilizar dict para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma) de peliculas
'''

import os
os.system('cls')

import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t 1.- Crear \n\t 2.- Borrar \n\t 3.- Mostrar \n\t 4.- Agregar Caracteristica " \
    "\n\t 5.- Modificar Caracteristica \n\t 6.- Borrar una caracteristica \n\t 7.- Salir")
    opcion=input("\n\t Selecciona una opcion: ").upper()
    
    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPelicula()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.agregarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.modificarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "6":
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "7":
            print("\n\t Terminaste la ejecucion del programa gracias por usarlo")
            peliculas.borrarPantalla()
            opcion=False
        case _:
            print("\n\t Opcion no valida, por favor selecciona una opcion del menu")
            peliculas.esperarTecla()
            opcion=True