import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Paso 1: Crear un DataFrame con los datos de los clientes

# Creamos 10 clientes de entrenamiento
datos_gym = {
    "cliente_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "visitas_mes": [18, 2, 1, 20, 4, 15, 0, 12, 3, 22],
    "edad": [25, 45, 50, 30, 38, 22, 60, 29, 41, 35],
    "pago_mensual": [50, 80, 80, 50, 65, 50, 80, 50, 65, 50],
    "cancelo": [0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
}

df = pd.DataFrame(datos_gym)

# Paso 2: Limpieza y separación de variables con pandas y numpy

# Eliminamos la columna "cliente_id" ya que no es relevante para el modelo
x = df[["visitas_mes", "edad", "pago_mensual"]]
y = df["cancelo"]

# Convertimos los datos a arrays de numpy para que sean compatibles con scikit-learn
X_np = x.to_numpy()
y_np = y.to_numpy()

# Paso 3: Escalado de características con Feature Scaling
xcaler = StandardScaler()
x_Scaled = xcaler.fit_transform(X_np)

# Paso 4: Preparación de los datos para entrenamiento y prueba
modelo_gym = LogisticRegression()
modelo_gym.fit(x_Scaled, y_np)

# Paso 5: Predicción sobre clientes nuevos
nuevos_clientes = np.array(
    [
        [16, 28, 50],  # Cliente 1: 16 visitas, 28 años, pago mensual de 50
        [1, 52, 80],   # Cliente 2: 1 visita, 52 años, pago mensual de 80
        [5, 33, 65],   # Cliente 3: 5 visitas, 33 años, pago mensual de 65
        [12, 40, 50],  # Cliente 4: 12 visitas, 40 años, pago mensual de 50
        [0, 60, 80],   # Cliente 5: 0 visitas, 60 años, pago mensual de 80
        [8, 25, 50],   # Cliente 6: 8 visitas, 25 años, pago mensual de 50
        [3, 45, 65],   # Cliente 7: 3 visitas, 45 años, pago mensual de 65
        [20, 30, 50],  # Cliente 8: 20 visitas, 30 años, pago mensual de 50
        [2, 55, 80],   # Cliente 9: 2 visitas, 55 años, pago mensual de 80
        [10, 35, 65],  # Cliente 10: 10 visitas, 35 años, pago mensual de 65
    ]
)

nuevos_clientes_scaled = xcaler.transform(nuevos_clientes)

# Predicción
predicciones = modelo_gym.predict(nuevos_clientes_scaled)
probabilidades = modelo_gym.predict_proba(nuevos_clientes_scaled)[:, 1]  # Probabilidad de cancelar

# Dataframe final con resultados
df_resultados = pd.DataFrame(nuevos_clientes, columns=x.columns)
df_resultados["prediccion_cancela"] = predicciones
df_resultados["riesgo_%"] = (probabilidades * 100).round(2)

print(df_resultados)