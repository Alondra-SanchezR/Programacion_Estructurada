#Dict u objeto que permita almacenar los siguientes atributos: (nombre, categoria, clasificacion, genero, idioma)

#pelicula = {
#    "nombre": "",
#    "categoria": "",
#    "clasificacion": "",
#    "genero": "",
#    "idioma": ""

pelicula={}

def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\n\t Presiona una tecla para continuar...")

def crearPeliculas():
    borrarPantalla()
    print("\n\t\t\ Agregar Peliculas: ")
    pelicula.update({"nombre": input("\n\t Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria": input("\n\t Ingresa la categoria: ").upper().strip()})
    pelicula.update({"clasificacion": input("\n\t Ingresa la clasificacion: ").upper().strip()})
    pelicula.update({"genero": input("\n\t Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma": input("\n\t Ingresa el idioma: ").upper().strip()})
    print("\n\t LA OPERACION SE REALIZO CON EXITO")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t\t\ Mostrar Peliculas: ")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\n\t {i}: {pelicula[i]}")
    else:
        print("\n\t No hay peliculas registradas")

def borrarPelicula():
    borrarPantalla()
    print("\n\t\t\ Borrar o Quitar la Pelicula: ")
    if len(pelicula) > 0:
        resp= input("\n\t Deseas borrar la pelicula? (S/N): ").upper().strip()
        if resp == "S":
            pelicula.clear()
            print("\n\t La pelicula se ha borrado con exito")
    else:
        print("\n\t No hay peliculas registradas")

            
def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t\ Agregar Caracteristica a la Pelicula: " )
    if len(pelicula) > 0:
        atributo = input("\n\t Ingresa el nombre de la caracteristica quedeseas agregar: ").lower().strip()
        valor_atributo = input(f"\n\t Ingresa el valor para {atributo}: ").upper().strip()
        pelicula[atributo] = valor_atributo
        print("\n\t La caracteristica se ha agregado con exito")

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t\t Modificar Caracteristica de la Pelicula: " )
    if len(pelicula) > 0:
        resp="SI"
        while resp=="SI":
            for i in pelicula:
                resp= input(f"\n\t Deseas modificar la caracteristica {i}? (Si/No): ").upper().strip()
                if resp == "SI":
                    valor_modificado = input(f"\n\t Ingresa el nuevo valor para {i}: ").upper().strip()
                    pelicula[i] = valor_modificado
                    print("\n\t La caracteristica se modifico con exito ")
                    esperarTecla()
    else:
        print("\n\t No hay peliculas en el sistema ")

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t\t Borrar Caracteristicas a Peliculas: " )
    if len(pelicula) > 0:
        print(f"\n\t Caracteristicas actuales: {i}: {pelicula[i]}")
        resp="SI"
        while resp=="SI":
         for i in pelicula:
            resp= input(f"\n\t Deseas borrar alguna caracteristica {i} ? (Si/No): ").upper().strip()
            if resp == "SI":
                borrar_valor= input(f"\n\t Ingresa la caracteristica que deseas borrar o quitar {i}: ").upper().strip()
                pelicula[i] = borrar_valor
                pelicula.clear()
                print("\n\t La caracteristica se borro con exito ")
    else:
        print("\n\t No hay caracteristicas para borrar ")