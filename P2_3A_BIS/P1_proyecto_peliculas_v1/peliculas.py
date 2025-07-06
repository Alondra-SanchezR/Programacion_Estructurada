peliculas=[]

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("Oprima cualquier tecla para continuar")

def agregarPeliculas():
    borrarPantalla()
    print("Agregar peliculas")
    peliculas.append(input("Ingresa el nombre: ")).upper().strip()
    print("¡LA OPERACION SE REALIZO CON EXITO!")

def mostarPeliculas():
    borrarPantalla()
    print(peliculas)
    print("Mostrar todas las peliculas")
    if len(peliculas)>0:
      for i in range(0, len (peliculas)):
        print(f"(i+1) : (peliculas[i]")

def limpiarPeliculas():
    borrarPantalla()
    print("\n\t Limpiar o borrar TODAS las peliculas: \n")
    resp=input("Deseas borrar todas las pelicoclas del sistema (Si/No)").lower

def buscarPeliculas():
   borrarPantalla()
   print("\n\t Buscar Peliculas: \n")
   pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar ").upper().strip()
   if not (pelicula_buscar in peliculas):
      print("\n\t Esta pelicula a buscar no existe en el sistema : ")
   else:
      encontro=0
      for i in range(0, len(peliculas)):
         if pelicula_buscar==peliculas[i]:
            print(f"\n\t La pelicula (pelicula_buscar) se encontro en el casillero: [i+1]")

def buscarPeliculas():
   borrarPantalla()
   print("\n\t Buscar Peliculas: \n")
   pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar ").upper().strip()
   encontro=0
   if not (pelicula_buscar in peliculas):
      print("\n\t Esta pelicula a buscar no existe en el sistema : ")
   else:
      for i in range(0, len(peliculas)):
         if pelicula_buscar==peliculas[i]:
            resp=input("Deseas actualizar la pelicula? (Si/No) ").lower()
            if resp=="si":
               peliculas[i]=input("\n\t Introduce el nuevo nombre de la pelicula: ").upper().strip()
               encontro+=1
               print("¡LA OPERACION SE REALIZO CON EXITO!")

print(f"Se modifico (encontro) pelicula(s) con este titulo")

def borrarPeliculas():
   borrarPantalla()
   print("\n\t Buscar Peliculas: \n")
   pelicula_borrar=input("Ingrese el nombre de la pelicula a borrar: ").upper().strip()
   encontro=0
   if not (pelicula_borrar in peliculas):
      print("\n\t Esta pelicula a borrar no existe en el sistema : ")
   else:
      for i in range(0, len(peliculas)):
         if pelicula_borrar==peliculas[i]:
            resp=input("Deseas quitar o borrar la pelicula del sistema? (Si/No) ").lower()
            if resp=="si":
               peliculas[i]=input("\n\t Introduce el nuevo nombre de la pelicula: ").upper().strip()
               encontro-=1
               peliculas.remove(encontro)
               print("La pelicula fue borrada con exito")

print(f"Se borraron (encontro) pelicula(s) con este titulo")