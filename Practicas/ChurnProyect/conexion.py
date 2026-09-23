from sqlalchemy import create_engine


# 1. CONEXIÓN A SQL SERVER Y EXTRACCIÓN DE DATOS
servidor = "localhost"  
base_datos = "ChurnDB"

engine = create_engine(
    f"mssql+pyodbc://@{servidor}/{base_datos}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)


query = """
SELECT 
    c.cliente_id,
    ISNULL(SUM(s.tiempo_sitio_min), 0) AS tiempo_en_tienda,
    COUNT(DISTINCT co.compra_id) AS cantidad_compras,
    COUNT(d.devolucion_id) AS devoluciones
FROM clientes c
LEFT JOIN sesiones s ON c.cliente_id = s.cliente_id
LEFT JOIN compras co ON c.cliente_id = co.cliente_id
LEFT JOIN devoluciones d ON co.compra_id = d.compra_id
GROUP BY c.cliente_id;
"""