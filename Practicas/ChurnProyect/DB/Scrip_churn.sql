CREATE DATABASE ChurnDB
ON PRIMARY 
(
	NAME = N'ChurnDB_Data',
	FILENAME = 'C:\Users\jluis.THE_BEST\Documents\UNIVERSIDAD\Cuatrimestre 1\Inteligencia Artificial\Proyectos\Bloque 3\Practicas\ChurnProyect\DB\ChurnDB.mdf',
	SIZE = 100MB,
	MAXSIZE = 5GB,
	FILEGROWTH = 64MB
)
LOG ON
(
	NAME = N'ChurnDB_log',
	FILENAME = 'C:\Users\jluis.THE_BEST\Documents\UNIVERSIDAD\Cuatrimestre 1\Inteligencia Artificial\Proyectos\Bloque 3\Practicas\ChurnProyect\DB\ChurnDB.ldf',
	SIZE = 32MB,
	MAXSIZE = 2GB,
	FILEGROWTH = 32MB
)
COLLATE Modern_Spanish_100_CI_AS;
GO

SELECT 
    servicename,
    service_account
FROM sys.dm_server_services;

Create table clientes
(
	cliente_id int primary key identity,
	nombre varchar(60),
	email varchar(100),
	fecha_registro DATE
);

create table sesiones
(
	sesion_id int primary key identity,
	cliente_id int,
	tiempo_sitio_min int,
	productos_vistos int,
	fecha_sesion DATE,
	foreign key (cliente_id) references clientes (cliente_id)
);

create table compras
(
	compra_id int primary key identity,
	cliente_id int,
	monto_carrito decimal(10,2),
	estado_compra varchar(50),
	fecha_compra DATE,
	foreign key (cliente_id) references clientes (cliente_id)
);

create table devoluciones
(
	devolucion_id int primary key identity,
	compra_id int,
	motivo varchar(150),
	fecha_devolucion DATE,
	foreign key (compra_id) references compras (compra_id)
);

use ChurnDB;


INSERT INTO clientes (nombre, email, fecha_registro)
VALUES
('José García', 'jose.garcia@email.com', '2025-01-05'),
('María López', 'maria.lopez@email.com', '2025-01-08'),
('Carlos Hernández', 'carlos.hernandez@email.com', '2025-01-12'),
('Ana Martínez', 'ana.martinez@email.com', '2025-01-15'),
('Luis González', 'luis.gonzalez@email.com', '2025-01-20'),
('Sofía Rodríguez', 'sofia.rodriguez@email.com', '2025-01-23'),
('Miguel Pérez', 'miguel.perez@email.com', '2025-01-28'),
('Laura Sánchez', 'laura.sanchez@email.com', '2025-02-02'),
('Diego Ramírez', 'diego.ramirez@email.com', '2025-02-05'),
('Fernanda Torres', 'fernanda.torres@email.com', '2025-02-09'),

('Jorge Flores', 'jorge.flores@email.com', '2025-02-12'),
('Daniela Rivera', 'daniela.rivera@email.com', '2025-02-15'),
('Ricardo Gómez', 'ricardo.gomez@email.com', '2025-02-19'),
('Valeria Díaz', 'valeria.diaz@email.com', '2025-02-22'),
('Andrés Cruz', 'andres.cruz@email.com', '2025-02-25'),
('Gabriela Morales', 'gabriela.morales@email.com', '2025-03-01'),
('Alejandro Ortiz', 'alejandro.ortiz@email.com', '2025-03-04'),
('Paola Reyes', 'paola.reyes@email.com', '2025-03-08'),
('Fernando Vargas', 'fernando.vargas@email.com', '2025-03-12'),
('Camila Mendoza', 'camila.mendoza@email.com', '2025-03-16'),

('Roberto Castro', 'roberto.castro@email.com', '2025-03-20'),
('Natalia Guerrero', 'natalia.guerrero@email.com', '2025-03-24'),
('Eduardo Rojas', 'eduardo.rojas@email.com', '2025-03-28'),
('Regina Navarro', 'regina.navarro@email.com', '2025-04-01'),
('Sergio Jiménez', 'sergio.jimenez@email.com', '2025-04-05'),
('Melissa Silva', 'melissa.silva@email.com', '2025-04-09'),
('Arturo Vargas', 'arturo.vargas2@email.com', '2025-04-13'),
('Daniela Mendoza', 'daniela.mendoza2@email.com', '2025-04-17'),
('Héctor Ramírez', 'hector.ramirez@email.com', '2025-04-21'),
('Patricia Torres', 'patricia.torres@email.com', '2025-04-25'),

('Manuel Ortega', 'manuel.ortega@email.com', '2025-04-29'),
('Carolina Vega', 'carolina.vega@email.com', '2025-05-03'),
('Óscar Navarro', 'oscar.navarro@email.com', '2025-05-07'),
('Andrea Campos', 'andrea.campos@email.com', '2025-05-11'),
('Francisco Luna', 'francisco.luna@email.com', '2025-05-15'),
('Diana Cabrera', 'diana.cabrera@email.com', '2025-05-19'),
('Raúl Medina', 'raul.medina@email.com', '2025-05-23'),
('Lucía Fuentes', 'lucia.fuentes@email.com', '2025-05-27'),
('Gustavo Salazar', 'gustavo.salazar@email.com', '2025-06-01'),
('Mariana Ponce', 'mariana.ponce@email.com', '2025-06-05'),

('Enrique Solís', 'enrique.solis@email.com', '2025-06-09'),
('Alejandra Cárdenas', 'alejandra.cardenas@email.com', '2025-06-13'),
('Iván Bautista', 'ivan.bautista@email.com', '2025-06-17'),
('Mónica Serrano', 'monica.serrano@email.com', '2025-06-21'),
('Adrián Valdez', 'adrian.valdez@email.com', '2025-06-25'),
('Karla Méndez', 'karla.mendez@email.com', '2025-06-29'),
('Óscar Castillo', 'oscar.castillo@email.com', '2025-07-03'),
('Verónica León', 'veronica.leon@email.com', '2025-07-07'),
('Pedro Márquez', 'pedro.marquez@email.com', '2025-07-11'),
('Claudia Rosales', 'claudia.rosales@email.com', '2025-07-15'),

('Javier Espinoza', 'javier.espinoza@email.com', '2025-07-19'),
('Isabel Franco', 'isabel.franco@email.com', '2025-07-23'),
('Mauricio Acosta', 'mauricio.acosta@email.com', '2025-07-27'),
('Silvia Miranda', 'silvia.miranda@email.com', '2025-07-31'),
('Gerardo Estrada', 'gerardo.estrada@email.com', '2025-08-04'),
('Rosa Ibarra', 'rosa.ibarra@email.com', '2025-08-08'),
('Hugo Nájera', 'hugo.najera@email.com', '2025-08-12'),
('Beatriz Valencia', 'beatriz.valencia@email.com', '2025-08-16'),
('Alberto Ochoa', 'alberto.ochoa@email.com', '2025-08-20'),
('Teresa Molina', 'teresa.molina@email.com', '2025-08-24'),

('Cristian Peña', 'cristian.pena@email.com', '2025-08-28'),
('Gabriela Paredes', 'gabriela.paredes@email.com', '2025-09-01'),
('Marco Antonio Ruiz', 'marco.ruiz@email.com', '2025-09-05'),
('Elena Sandoval', 'elena.sandoval@email.com', '2025-09-09'),
('Jonathan Nieto', 'jonathan.nieto@email.com', '2025-09-13'),
('Cecilia Arias', 'cecilia.arias@email.com', '2025-09-17'),
('Rafael Beltrán', 'rafael.beltran@email.com', '2025-09-21'),
('Adriana Solano', 'adriana.solano@email.com', '2025-09-25'),
('Víctor Meza', 'victor.meza@email.com', '2025-09-29'),
('Lorena Duarte', 'lorena.duarte@email.com', '2025-10-03'),

('Martín Zamora', 'martin.zamora@email.com', '2025-10-07'),
('Gloria Treviño', 'gloria.trevino@email.com', '2025-10-11'),
('Salvador Castañeda', 'salvador.castaneda@email.com', '2025-10-15'),
('Nora Villarreal', 'nora.villarreal@email.com', '2025-10-19'),
('Tomás Cordero', 'tomas.cordero@email.com', '2025-10-23'),
('Estefanía Vázquez', 'estefania.vazquez@email.com', '2025-10-27'),
('Ramón Galindo', 'ramon.galindo@email.com', '2025-10-31'),
('Brenda Tapia', 'brenda.tapia@email.com', '2025-11-04'),
('Alonso Miranda', 'alonso.miranda@email.com', '2025-11-08'),
('Fabiola Núñez', 'fabiola.nunez@email.com', '2025-11-12'),

('Emiliano Cabrera', 'emiliano.cabrera@email.com', '2025-11-16'),
('Jimena Soto', 'jimena.soto@email.com', '2025-11-20'),
('Mateo Rangel', 'mateo.rangel@email.com', '2025-11-24'),
('Renata Salinas', 'renata.salinas@email.com', '2025-11-28'),
('Rodrigo Correa', 'rodrigo.correa@email.com', '2025-12-02'),
('Paulina Trejo', 'paulina.trejo@email.com', '2025-12-06'),
('Germán Patiño', 'german.patino@email.com', '2025-12-10'),
('Montserrat Lara', 'montserrat.lara@email.com', '2025-12-14'),
('Félix Domínguez', 'felix.dominguez@email.com', '2025-12-18'),
('Marisol Carrillo', 'marisol.carrillo@email.com', '2025-12-22'),

('Nicolás Durán', 'nicolas.duran@email.com', '2025-12-26'),
('Regina Salgado', 'regina.salgado@email.com', '2025-12-28'),
('Esteban Molina', 'esteban.molina@email.com', '2025-12-29'),
('Verónica Pacheco', 'veronica.pacheco@email.com', '2025-12-30'),
('Julián Peralta', 'julian.peralta@email.com', '2025-12-31'),
('Mariana Valdés', 'mariana.valdes@email.com', '2026-01-02'),
('Sebastián Mora', 'sebastian.mora@email.com', '2026-01-04'),
('Ximena Lozano', 'ximena.lozano@email.com', '2026-01-06'),
('Ángel Carrasco', 'angel.carrasco@email.com', '2026-01-08'),
('Natalia Cabrera', 'natalia.cabrera@email.com', '2026-01-10');


INSERT INTO sesiones
    (cliente_id, tiempo_sitio_min, productos_vistos, fecha_sesion)
SELECT
    cliente_id,
    5 + (cliente_id * 3 % 56),
    1 + (cliente_id % 10),
    DATEADD(DAY, cliente_id % 30, '2025-09-01')
FROM clientes;




INSERT INTO sesiones
    (cliente_id, tiempo_sitio_min, productos_vistos, fecha_sesion)
SELECT
    cliente_id,
    10 + (cliente_id * 7 % 71),
    2 + (cliente_id * 2 % 15),
    DATEADD(DAY, (cliente_id + 10) % 30, '2025-09-01')
FROM clientes;

INSERT INTO compras
    (cliente_id, monto_carrito, estado_compra, fecha_compra)
SELECT
    ((cliente_id - 1) % 75) + 1,
    CAST(200 + ((cliente_id - 1) * 137 % 4801) AS DECIMAL(10,2)),
    CASE
        WHEN cliente_id % 5 = 0 THEN 'Cancelada'
        WHEN cliente_id % 4 = 0 THEN 'Pendiente'
        WHEN cliente_id % 3 = 0 THEN 'Enviada'
        ELSE 'Completada'
    END,
    DATEADD(DAY, cliente_id % 120, '2025-05-01')
FROM
(
    SELECT TOP 150
        ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS cliente_id
    FROM sys.objects a
    CROSS JOIN sys.objects b
) AS x;


INSERT INTO devoluciones
    (compra_id, motivo, fecha_devolucion)
SELECT
    compra_id,
    CASE compra_id % 5
        WHEN 0 THEN 'Producto defectuoso'
        WHEN 1 THEN 'Producto incorrecto'
        WHEN 2 THEN 'No era lo esperado'
        WHEN 3 THEN 'Producto dañado'
        ELSE 'Cambio de opinión'
    END,
    DATEADD(DAY, 5 + (compra_id % 15), fecha_compra)
FROM compras
WHERE compra_id % 3 = 0
  AND compra_id <= 150;



SELECT 'Clientes' AS tabla, COUNT(*) AS cantidad
FROM clientes

UNION ALL

SELECT 'Sesiones', COUNT(*)
FROM sesiones

UNION ALL

SELECT 'Compras', COUNT(*)
FROM compras

UNION ALL

SELECT *
FROM devoluciones;

SELECT 
    c.cliente_id,
    SUM(s.tiempo_sitio_min) AS tiempo_en_tienda,
    COUNT(DISTINCT co.compra_id) AS cantidad_compras,
    COUNT(d.devolucion_id) AS devoluciones
FROM clientes c
LEFT JOIN sesiones s ON c.cliente_id = s.cliente_id
LEFT JOIN compras co ON c.cliente_id = co.cliente_id
LEFT JOIN devoluciones d ON co.compra_id = d.compra_id
GROUP BY c.cliente_id;