"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#1.- Funcion que no recibe parametros y no regresa valor

def solicitarDatos1():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    print(f"El nombre es: {nombre} y su telefono es: {telefono}")

#3.- Funcion que recibe parametros y no regresa valor
    
def solicitarDatos3(nom,tel):
    nombre=nom
    telefono=tel 
    print(f"El nombre es: {nom} y su telefono es: {tel}")

#2.- Funcion que no recibe parametros y regresa valor

def solicitarDatos2():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    return nombre,telefono 

#4.- Funcion que recibe parametros y regresa valor

def solicitarDatos4(nom,tel):
    nombre=nom
    telefono=tel 
    return nombre,telefono

#Llamar mis funciones
solicitarDatos1()

nom3=input("Nombre: ")
tel3=input("Telefono: ")
solicitarDatos3(nom3,tel3)

nom2,tel2=solicitarDatos2()
print(f"\tNombre: {nom2} \n \tTelefono: {tel2}")

nom4=input("Nombre: ")
tel4=input("Telefono: ")
nombre4,telefono4=solicitarDatos4(nom4,tel4)
print(f"\tNombre: {nombre4} \n \tTelefono: {telefono4}")