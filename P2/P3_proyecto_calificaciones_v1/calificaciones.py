calificacion = {}

def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\n" + "\t" * 4 + "🕹️  Presiona cualquier tecla para continuar... ")

def menu_principal():
    print("\n" + "\t" * 3 + "🎓✨═══════════════════════════════════════════════")
    print("\t" * 3 + "       SISTEMA DE CALIFICACIONES        ")
    print("\t" * 3 + "═══════════════════════════════════════════════✨🎓\n")
    print("\t" * 4 + "1️⃣  📥 Agregar calificaciones")
    print("\t" * 4 + "2️⃣  📋 Mostrar calificaciones")
    print("\t" * 4 + "3️⃣  📊 Calcular promedio")
    print("\t" * 4 + "4️⃣  🔍 Buscar")
    print("\t" * 4 + "5️⃣  ❌ Salir\n")
    return input("\t" * 4 + "🔽 Elige una opción (1-5): ")

def agregar_calificacion(lista):
    borrarPantalla()
    print("\n" + "\t" * 4 + "➕════════════ AGREGAR CALIFICACIONES ════════════➕\n")
    nombre = input("\t" * 4 + "👤 Nombre del alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        while True:
            try:
                cal = float(input(f"\n\t" * 4 + f"📚 Calificación {i}: "))
                if 0 <= cal <= 10:
                    calificaciones.append(cal)
                    break
                else:
                    print("\n" + "\t" * 4 + "❌ Error: La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("\n" + "\t" * 4 + "🚫 Entrada inválida. Debe ser un número.")
    lista.append([nombre] + calificaciones)
    print("\n" + "\t" * 4 + "✅ Calificaciones agregadas exitosamente ✅\n")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("\n" + "\t" * 4 + "📖═════════ LISTADO DE CALIFICACIONES ═════════📖\n")
    if lista:
        encabezado = f"{'👨‍🎓 Nombre':<20}{'📝 Calif. 1':<15}{'📝 Calif. 2':<15}{'📝 Calif. 3':<15}"
        print("\t" * 3 + encabezado)
        print("\t" * 3 + "-" * len(encabezado))
        for fila in lista:
            print("\t" * 3 + f"{fila[0]:<20}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
        print("\t" * 3 + "-" * len(encabezado))
        print(f"\n\t" * 4 + f"📌 Total de alumnos registrados: {len(lista)}\n")
    else:
        print("\t" * 4 + "⚠️  No hay calificaciones registradas.\n")

def calcular_promedio(lista):
    borrarPantalla()
    print("\n" + "\t" * 4 + "📊═════════ PROMEDIOS GENERALES ═════════📊\n")
    if lista:
        encabezado = f"{'👨‍🏫 Nombre':<20}{'📈 Promedio':<12}"
        print("\t" * 3 + encabezado)
        print("\t" * 3 + "-" * len(encabezado))
        promedio_grupal = 0 
        for fila in lista:
            nombre = fila[0]
            promedio = sum(fila[1:]) / 3
            print("\t" * 3 + f"{nombre:<20}{promedio:<12.2f}")
            promedio_grupal += promedio
        promedio_grupal /= len(lista)
        print("\t" * 3 + "-" * len(encabezado))
        print(f"\n\t" * 4 + f"🏆 Promedio general del grupo: {promedio_grupal:.2f}\n")
    else:
        print("\t" * 4 + "⚠️  No hay registros para calcular promedio.\n")
        print("\t\t\t⚠️  No hay calificaciones registradas.\n")
