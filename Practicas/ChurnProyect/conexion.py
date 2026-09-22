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

# df_clientes = pd.read_sql(query, engine)
# print("--- DATOS EXTRAÍDOS DE SQL SERVER ---")
# print(df_clientes.head())


# # 2. DEFINIR VARIABLE OBJETIVO Y VARIABLES PREDICTORAS
# df_clientes['churn'] = np.where(
#     (df_clientes["devoluciones"] >= 2)
#     | (df_clientes["tiempo_en_tienda"] < 10),
#     1,
#     0
# )

# x = df_clientes[["tiempo_en_tienda", "cantidad_compras", "devoluciones"]]
# y = df_clientes["churn"]

# # 3. DIVIDIR LOS DATOS EN CONJUNTOS DE ENTRENAMIENTO Y PRUEBA
# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# scaler = StandardScaler()
# x_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# modelo_churn = LogisticRegression()
# modelo_churn.fit(x_train_scaled, y_train)

# # 4. VALIDACIÓN DEL MODELO CON MATRIZ DE CONFUSIÓN
# y_pred = modelo_churn.predict(X_test_scaled)
# matriz = confusion_matrix(y_test, y_pred)

# plt.figure(figsize=(5, 4))
# sns.heatmap(
#     matriz,
#     annot=True,
#     fmt="d",
#     cmap="Blues",
#     xticklabels=["Retenido (0)", "Abandono (1)"],
#     yticklabels=["Retenido (0)", "Abandono (1)"],
# )
# plt.title("Matriz de Confusión - SQL Server Data")
# plt.xlabel("Predicción del Modelo")
# plt.ylabel("Realidad")
# plt.tight_layout()
# plt.show()