calificacion={}

def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\t\t\t\t :::. ➤ Oprima cualquier tecla para continuar... ⏭️")

def menu_principal():
    print("\n\t\t\t\t🎓✨ .::: SISTEMA DE CALIFICACIONES :::. ✨🎓\n")
    print("\t\t\t\t\t ➊ 📥 Agregar calificaciones")
    print("\t\t\t\t\t ➋ 📋 Mostrar calificaciones")
    print("\t\t\t\t\t ➌ 📊 Calcular promedio")
    print("\t\t\t\t\t ➍ 🔎 Buscar")
    print("\t\t\t\t\t ➎ ❌ Salir\n")
    opcion = input("\t\t\t\t\t🔽 Elige una opción (1-5): ")
    return opcion

def agregar_calificacion(lista):
    borrarPantalla()
    print("\t\t\t\t➕ .:: AGREGAR CALIFICACIONES ::. ➕\n")
    nombre = input("\t\t\t👤 Nombre del alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        continua = True
        while continua:
            try:
                cal = float(input(f"\n\t\t\t📚 Calificación {i}: "))
                if 0 <= cal <= 10:
                    calificaciones.append(cal)
                    break
                else:
                    print("\n\t\t\t❌ Error: La calificación debe estar entre 0 y 10 ❌")
            except ValueError:
                print("\n\t\t\t🚫 Entrada inválida. Debe ser un valor numérico  🚫")
    lista.append([nombre] + calificaciones)
    print("\n\t\t\t✅ Calificaciones agregadas exitosamente ✅\n")

def mostrar_calificaciones(lista):
    ancho = 115
    borrarPantalla()
    print("\t\t\t\t📖 .:: MOSTRAR CALIFICACIONES ::. 📖\n")
    if len(lista) > 0:
        print(f"\t\t\t{'👨‍🎓 Nombre':<20}{'📝 Calif. 1':<12}{'📝 Calif. 2':<12}{'📝 Calif. 3':<12}")
        print(("-" * 60).center(115))
        for fila in lista:
            print(f"\t\t\t\t{fila[0]:<15}{fila[1]:<12}{fila[2]:<12}{fila[3]:<12}")
        print(("-" * 60).center(ancho))
        cuantos = len(lista)
        print(f"\n\t\t\t📌 Total de alumnos registrados: {cuantos} \n")
    else:
        print("\t\t\t\t⚠️  No hay calificaciones registradas.\n")

def calcular_promedio(lista):
    borrarPantalla()
    ancho = 90
    print("\t\t\t\t📊 .:: PROMEDIOS GENERALES ::. 📊\n")
    if len(lista) > 0:
        print(f"\t\t\t{'👨‍🏫 Nombre':<20}{'📈 Promedio':<12}")
        print(("-" * 32).center(90))
        promedio_grupal = 0 
        for fila in lista:
            nombre = fila[0]
            promedio = sum(fila[1:]) / 3
            print(f"\t\t\t\t{nombre:<15}{promedio:<12.2f}")
            promedio_grupal += promedio
        print(("-" * 32).center(ancho))
        promedio_grupal = promedio_grupal / len(lista)
        print(f"\n\t\t\t🏆 Promedio general del grupo: {promedio_grupal:.2f}\n")
    else:
        print("\t\t\t⚠️  No hay calificaciones registradas.\n")