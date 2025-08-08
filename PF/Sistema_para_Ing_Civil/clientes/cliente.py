from conexionBD import conexion, cursor

def agregar_cliente(nombre, telefono, direccion, correo, usuario_id):
    try:
        cursor.execute("""
            INSERT INTO clientes (nombre, telefono, direccion, correo, usuario_id)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, telefono, direccion, correo, usuario_id))
        conexion.commit()
        return True
    except Exception as e:
        print(f"❌ Error al agregar cliente: {e}")
        return False

def obtener_clientes(usuario_id):
    try:
        cursor.execute("""
            SELECT id, nombre, telefono, direccion, correo FROM clientes
            WHERE usuario_id = %s
        """, (usuario_id,))
        return cursor.fetchall()
    except Exception as e:
        print(f"❌ Error al obtener clientes: {e}")
        return []

def actualizar_cliente(cliente_id, nombre, telefono, direccion, correo):
    try:
        cursor.execute("""
            UPDATE clientes SET nombre=%s, telefono=%s, direccion=%s, correo=%s
            WHERE id = %s
        """, (nombre, telefono, direccion, correo, cliente_id))
        conexion.commit()
        return True
    except Exception as e:
        print(f"❌ Error al actualizar cliente: {e}")
        return False

def eliminar_cliente(cliente_id):
    try:
        cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
        conexion.commit()
        return True
    except Exception as e:
        print(f"❌ Error al eliminar cliente: {e}")
        return False
