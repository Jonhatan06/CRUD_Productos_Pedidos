CREATE TABLE IF NOT EXISTS clientes (
 id_cliente SERIAL PRIMARY KEY,
 nombre VARCHAR(100) NOT NULL,
 email VARCHAR(100),
 ciudad VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS productos (
 id_producto SERIAL PRIMARY KEY,
 nombre VARCHAR(100) NOT NULL,
 precio NUMERIC(12,2) NOT NULL,
 stock INTEGER
);
CREATE TABLE IF NOT EXISTS pedidos (
 id_pedido SERIAL PRIMARY KEY,
 id_cliente INTEGER REFERENCES clientes(id_cliente),
 id_producto INTEGER REFERENCES productos(id_producto),
 cantidad INTEGER NOT NULL,
 fecha DATE DEFAULT CURRENT_DATE
);
INSERT INTO clientes (nombre,email,ciudad)
SELECT 'Cliente de prueba','cliente@ejemplo.com','Asuncion'
WHERE NOT EXISTS (SELECT 1 FROM clientes);
