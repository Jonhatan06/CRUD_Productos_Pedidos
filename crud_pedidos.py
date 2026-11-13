from conexion import conectar

def insertar_pedido():
    cliente = int(input('ID del cliente existente: '))
    producto = int(input('ID del producto existente: '))
    cantidad = int(input('Cantidad: '))
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute('INSERT INTO pedidos (id_cliente, id_producto, cantidad) VALUES (%s, %s, %s) RETURNING id_pedido', (cliente, producto, cantidad))
            identificador = cursor.fetchone()[0]
        conexion.commit()
    print(f'Pedido agregado correctamente. ID: {identificador}')

def listar_pedidos():
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute('SELECT id_pedido, id_cliente, id_producto, cantidad, fecha FROM pedidos ORDER BY id_pedido')
            filas = cursor.fetchall()
    print('\nPEDIDOS:')
    for fila in filas:
        print(f'ID: {fila[0]} | Cliente: {fila[1]} | Producto: {fila[2]} | Cantidad: {fila[3]} | Fecha: {fila[4]}')
    if not filas:
        print('No hay pedidos registrados.')

def actualizar_pedido():
    identificador = int(input('ID del pedido a modificar: '))
    cantidad = int(input('Nueva cantidad: '))
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute('UPDATE pedidos SET cantidad = %s WHERE id_pedido = %s', (cantidad, identificador))
            modificados = cursor.rowcount
        conexion.commit()
    print('Pedido actualizado correctamente.' if modificados else 'No existe ese pedido.')
    listar_pedidos()

def eliminar_pedido():
    identificador = int(input('ID del pedido a eliminar: '))
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute('DELETE FROM pedidos WHERE id_pedido = %s', (identificador,))
            eliminados = cursor.rowcount
        conexion.commit()
    print('Pedido eliminado correctamente.' if eliminados else 'No existe ese pedido.')
    listar_pedidos()

if __name__ == '__main__':
    while True:
        print('\n--- CRUD PEDIDOS ---')
        print('1. Insertar pedido')
        print('2. Listar pedidos')
        print('3. Actualizar pedido')
        print('4. Eliminar pedido')
        print('0. Salir')
        opcion = input('Elegí una opción: ')
        try:
            if opcion == '1': insertar_pedido()
            elif opcion == '2': listar_pedidos()
            elif opcion == '3': actualizar_pedido()
            elif opcion == '4': eliminar_pedido()
            elif opcion == '0': break
            else: print('Opción incorrecta.')
        except Exception as error:
            print('Error:', error)
