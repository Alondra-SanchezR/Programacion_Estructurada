from conexionBD import conexion, cursor

def agregar_proyecto(nombre, ubicacion, presupuesto, materiales, tareas, cliente_id):
    try:
        materiales_str = ', '.join(materiales)
        tareas_str = ', '.join(tareas)
        cursor.execute("""
            INSERT INTO proyectos (nombre, ubicacion, presupuesto, materiales, tareas, cliente_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nombre, ubicacion, presupuesto, materiales_str, tareas_str, cliente_id))
        conexion.commit()
        return True
    except Exception as e:
        print(f"❌ Error al agregar proyecto: {e}")
        return False

def obtener_proyectos(cliente_id):
    try:
        cursor.execute("""
            SELECT id, nombre, ubicacion, presupuesto, materiales, tareas
            FROM proyectos WHERE cliente_id = %s
        """, (cliente_id,))
        return cursor.fetchall()
    except Exception as e:
        print(f"❌ Error al obtener proyectos: {e}")
        return []

def actualizar_proyecto(pid, nombre, ubicacion, presupuesto, materiales, tareas):
    try:
        materiales_str = ', '.join(materiales)
        tareas_str = ', '.join(tareas)
        cursor.execute("""
            UPDATE proyectos SET nombre=%s, ubicacion=%s, presupuesto=%s,
            materiales=%s, tareas=%s WHERE id=%s
        """, (nombre, ubicacion, presupuesto, materiales_str, tareas_str, pid))
        conexion.commit()
        return True
    except Exception as e:
        print(f"❌ Error al actualizar proyecto: {e}")
        return False

def eliminar_proyecto(pid):
    try:
        cursor.execute("DELETE FROM proyectos WHERE id = %s", (pid,))
        conexion.commit()
        return True
    except Exception as e:
        print(f"❌ Error al eliminar proyecto: {e}")
        return False
