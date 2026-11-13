
from conexion import conectar


# PASO 2: VERIFICAR CONEXION
def verificar_conexion():
    conexion = conectar()

    if conexion:
        print("Conexion con PostgreSQL exitosa.")
        conexion.close()
        return True
    else:
        print("Error al conectar con PostgreSQL.")
        return False


# PASO 3: INSERTAR ALUMNOS

def insertar_alumnos():
    cantidad = int(input("Cantidad de alumnos a insertar: "))

    with conectar() as conexion:
        with conexion.cursor() as cursor:
            for i in range(cantidad):
                print(f"\n--- Alumno {i + 1} ---")

                nombre = input("Nombre: ")
                cedula = input("Cedula: ")
                carrera = input("Carrera: ")
                promedio = float(input("Promedio: "))

                cursor.execute(
                    """INSERT INTO alumnos
                    (nombre, cedula, carrera, promedio)
                    VALUES (%s, %s, %s, %s)""",
                    (nombre, cedula, carrera, promedio)
                )

        conexion.commit()

    print("\nAlumnos insertados correctamente.")



# PASO 4: LISTAR ALUMNOS
def listar_alumnos():
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM alumnos ORDER BY id_alumno"
            )
            alumnos = cursor.fetchall()

    print("\n--- LISTADO DE ALUMNOS ---")

    for alumno in alumnos:
        print(alumno)


# PASO 5: ACTUALIZAR ALUMNO
def actualizar_alumno():
    identificador = int(input("ID del alumno a modificar: "))
    carrera = input("Nueva carrera: ")
    promedio = float(input("Nuevo promedio: "))

    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                """UPDATE alumnos
                SET carrera = %s, promedio = %s
                WHERE id_alumno = %s""",
                (carrera, promedio, identificador)
            )
            cantidad = cursor.rowcount

        conexion.commit()

    if cantidad:
        print("Alumno actualizado correctamente.")
    else:
        print("No existe ese alumno.")

    listar_alumnos()


# PASO 6: ELIMINAR ALUMNO
def eliminar_alumno():
    identificador = int(input("ID del alumno a eliminar: "))

    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                "DELETE FROM alumnos WHERE id_alumno = %s",
                (identificador,)
            )
            cantidad = cursor.rowcount

        conexion.commit()

    if cantidad:
        print("Alumno eliminado correctamente.")
    else:
        print("No existe ese alumno.")

    listar_alumnos()


# MENU PRINCIPAL
def menu():
    if not verificar_conexion():
        return

    while True:
        print("\n===== CRUD ALUMNOS =====")
        print("1. Insertar alumnos")
        print("2. Listar alumnos")
        print("3. Actualizar alumno")
        print("4. Eliminar alumno")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            insertar_alumnos()

        elif opcion == "2":
            listar_alumnos()

        elif opcion == "3":
            actualizar_alumno()

        elif opcion == "4":
            eliminar_alumno()

        elif opcion == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opcion incorrecta.")


if __name__ == "__main__":
    menu()
