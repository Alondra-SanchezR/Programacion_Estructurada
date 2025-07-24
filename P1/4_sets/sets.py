"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("cls")

paises={"México","Brasil","España","Canada"}
print(paises)

varios={True,"UTD",33,3,14}
print(varios)

#Funcines u Operaciones
paises.add("Mexico")

paises.remove("Mexico")

#Ejemplo: Crear un programa que solicite los email de los alumnos
#de la UTD almacenar en una lista y posteriormente mostrar en 
#pantalla los email sin duplicados.

emails=[]

n=int(input("¿Cuántos correos desea ingresar?: "))

for i in range(n):
    correo = input(f"Ingrese el correo #{i+1}: ")
    emails.append(correo)

emails_unicos= set(emails)
print(emails_unicos)

#Propuesta 1:
resp="si"
emails=[]
while resp=="si":
    emails.append(input("Introduzca su email: "))
    resp=input("´¿Quiere agregar otro email? ")
print(emails)
emails_set=set(emails)
print(emails_set)
emails=list(emails_set)
