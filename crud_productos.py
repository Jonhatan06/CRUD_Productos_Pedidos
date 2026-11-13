from conexion import conectar

def insertar_producto():
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    stock = int(input('Stock: '))
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute('INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s) RETURNING id_producto', (nombre, precio, stock))
            identificador = cursor.fetchone()[0]
        conexion.commit()
    print(f'Producto agregado correctamente. ID: {identificador}')

def listar_productos():
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute('SELECT id_producto, nombre, precio, stock FROM productos ORDER BY id_producto')
            filas = cursor.fetchall()
    print('\nPRODUCTOS:')
    for fila in filas:
        print(f'ID: {fila[0]} | Nombre: {fila[1]} | Precio: {fila[2]} | Stock: {fila[3]}')
    if not filas:
        print('No hay productos registrados.')


def actualizar_producto():
    identificador = int(input('ID del producto a modificar: '))
    nombre = input('Nuevo nombre: ')
    precio = float(input('Nuevo precio: '))
    stock = int(input('Nuevo stock: '))
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute('UPDATE productos SET nombre = %s, precio = %s, stock = %s WHERE id_producto = %s', (nombre, precio, stock, identificador))
            cantidad = cursor.rowcount
        conexion.commit()
    print('Producto actualizado correctamente.' if cantidad else 'No existe ese producto.')
    listar_productos()


def eliminar_producto():
    identificador = int(input('ID del producto a eliminar: '))
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute('DELETE FROM productos WHERE id_producto = %s', (identificador,))
            cantidad = cursor.rowcount
        conexion.commit()
    print('Producto eliminado correctamente.' if cantidad else 'No existe ese producto.')
    listar_productos()

if __name__ == '__main__':
    while True:
        print('\n--- CRUD PRODUCTOS ---')
        print('1. Insertar producto')
        print('2. Listar productos')
        print('3. Actualizar producto')
        print('4. Eliminar producto')
        print('0. Salir')
        opcion = input('Elegí una opción: ')
        try:
            if opcion == '1': insertar_producto()
            elif opcion == '2': listar_productos()
            elif opcion == '3': actualizar_producto()
            elif opcion == '4': eliminar_producto()
            elif opcion == '0': break
            else: print('Opción incorrecta.')
        except (ValueError, Exception) as error:
            print('Error:', error)
