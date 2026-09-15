import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# 1. Cargar datos de entrenamiento
df_train = pd.read_csv("Practicas/train_eccomerce.csv")

columnas_features = ["tiempo_sitio_min", "productos_vistos", "monto_carrito"]
X_train = df_train[columnas_features]
y_train = df_train[
    "compra_alta"
]  # O la variable objetivo de compra

# 2. Escalar datos de entrenamiento
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# 3. Entrenar el modelo
modelo_ecommerce = LogisticRegression()
modelo_ecommerce.fit(X_train_scaled, y_train)

# 4. Cargar y transformar clientes nuevos
df_nuevos = pd.read_csv("Practicas/data_eccomerce.csv")
X_nuevos = df_nuevos[columnas_features]

X_nuevos_scaled = scaler.transform(X_nuevos)

# 5. Generar predicciones
df_nuevos["prediccion_clase"] = modelo_ecommerce.predict(X_nuevos_scaled)
df_nuevos["probabilidad_%"] = (
    modelo_ecommerce.predict_proba(X_nuevos_scaled)[:, 1] * 100
).round(2)

print(df_nuevos)