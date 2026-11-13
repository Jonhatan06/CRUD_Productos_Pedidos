# CRUD de Productos y Pedidos

**Trabajo práctico – Unidad V**  
**Asignatura:** Python Lenguaje I  
**Universidad Americana**  
**Estudiante:** Jonhatan Legal  
**Docente:** Prof. Mgtr. Alberto F. Giménez Méndez

## Descripción del proyecto

Este proyecto implementa un sistema CRUD (Crear, Leer, Actualizar y Eliminar) utilizando Python y PostgreSQL.

El sistema permite administrar dos tablas de una base de datos:

- **Productos:** registro, consulta, modificación y eliminación de productos.
- **Pedidos:** registro, consulta, actualización de cantidades y eliminación de pedidos.

La conexión entre Python y PostgreSQL se realiza mediante la librería `psycopg2`. PostgreSQL se ejecuta en un contenedor Docker.

## Tecnologías utilizadas

- Python 3
- PostgreSQL 17
- Docker Desktop
- Visual Studio Code
- psycopg2-binary
- python-dotenv
- Git y GitHub

## Estructura del proyecto

```text
CRUD_Productos_Pedidos/
│
├── conexion.py
├── crear_tablas.sql
├── crud_productos.py
├── crud_pedidos.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Requisitos previos

Para ejecutar el proyecto se necesita tener instalado:

- Python.
- Docker Desktop.
- Git (opcional).

## Instalación y configuración

### 1. Descargar el proyecto

Clonar el repositorio:

```bash
git clone https://github.com/Jonhatan06/CRUD_Productos_Pedidos.git
```

Ingresar a la carpeta:

```bash
cd CRUD_Productos_Pedidos
```

### 2. Crear el entorno virtual

```bash
python -m venv .venv
```

Activarlo en Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Iniciar PostgreSQL con Docker

Ejecutar:

```bash
docker run --name postgres-universidad -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=mi_password_local -e POSTGRES_DB=universidad -p 5433:5432 -v universidad_pgdata:/var/lib/postgresql/data -d postgres:17
```

### 5. Configurar las variables de entorno

Crear el archivo `.env` copiando el archivo de ejemplo:

```powershell
Copy-Item .env.example .env
```

Configurar las variables del archivo `.env` con los mismos datos utilizados al crear el contenedor:

```env
DB_HOST=127.0.0.1
DB_PORT=5433
DB_NAME=universidad
DB_USER=postgres
DB_PASSWORD=mi_password_local
```

**Importante:** el archivo `.env` contiene las credenciales locales y no debe publicarse en GitHub.

### 6. Crear las tablas

Ejecutar el archivo SQL dentro del contenedor:

```powershell
Get-Content .\crear_tablas.sql | docker exec -i postgres-universidad psql -U postgres -d universidad
```

### 7. Ejecutar los programas

Para iniciar el CRUD de productos:

```bash
python crud_productos.py
```

Para iniciar el CRUD de pedidos:

```bash
python crud_pedidos.py
```

## Operaciones implementadas

### CRUD de productos

| Operación | Descripción |
|---|---|
| INSERT | Agregar un producto con nombre, precio y stock. |
| SELECT | Listar los productos registrados. |
| UPDATE | Modificar nombre, precio y stock mediante su ID. |
| DELETE | Eliminar un producto mediante su ID. |

### CRUD de pedidos

| Operación | Descripción |
|---|---|
| INSERT | Registrar un pedido con cliente, producto y cantidad. |
| SELECT | Listar los pedidos registrados. |
| UPDATE | Modificar la cantidad de un pedido. |
| DELETE | Eliminar un pedido mediante su ID. |

## Consideraciones técnicas

- Se utilizan consultas parametrizadas mediante marcadores `%s`.
- Se utiliza `conexion.commit()` para confirmar las operaciones de escritura.
- Se emplean claves foráneas para relacionar pedidos con clientes y productos.
- Se utilizan menús interactivos para seleccionar las operaciones.
- Las conexiones a PostgreSQL se realizan desde Python mediante `psycopg2`.

## Autor

**Jonhatan Legal**

Trabajo práctico correspondiente a la Unidad V de Python Lenguaje I – Universidad Americana.