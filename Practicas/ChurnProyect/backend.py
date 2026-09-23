
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from conexion import engine, query
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def cargar_y_entrenar_modelo():
  # 1. Extraer datos de SQL Server
  # Leemos la conexion y ejecutamos la consulta(desde conexion.py) y la convertimos en un DataFrame de pandas
  df_clientes = pd.read_sql(query, engine)
  print("--- DATOS EXTRAÍDOS DE SQL SERVER ---")
  print(df_clientes.head())

  # 2. Definir la variable objetivo (churn)
  # Se crea la columna churn y agreegamos un condicinal de numpy para marcar a los clientes que cumplen con la condición de riesgo de fuga
  df_clientes["churn"] = np.where(
      # Condición: si el cliente tiene 2 o más devoluciones o ha pasado menos de 10 minutos en la tienda
      (df_clientes["devoluciones"] >= 2) | (df_clientes["tiempo_en_tienda"] < 10),
      1,
      0,
  ) # Condición: si el cliente tiene 2 o más devoluciones o ha pasado menos de 10 minutos en la tienda

  # Separamos las variables predictoras (X) de la variable objetivo (y)
  x = df_clientes[["tiempo_en_tienda", "cantidad_compras", "devoluciones"]]
  # Guardamos la variable objetivo (y) que indica si el cliente es churn o no
  y = df_clientes["churn"]

  # 3. Dividir datos y entrenar
  X_train, X_test, y_train, y_test = train_test_split(
      x, y, test_size=0.2, random_state=42
  )

  scaler = StandardScaler()
  x_train_scaled = scaler.fit_transform(X_train)
  X_test_scaled = scaler.transform(X_test)

  modelo_churn = LogisticRegression()
  modelo_churn.fit(x_train_scaled, y_train) # Aqui se aplica la Regresión Logística y la Función Sigmoide

  # 4. Predicciones y calculo de metricas 
  y_pred = modelo_churn.predict(X_test_scaled) # Aqui tambien se usan
  matriz = confusion_matrix(y_test, y_pred)

  accuracy = round(accuracy_score(y_test, y_pred) * 100, 2)
  precision = round(
    precision_score(y_test, y_pred, zero_division=0) * 100, 2
  )
  recall = round(recall_score(y_test, y_pred, zero_division=0) * 100, 2)

  # 5. Matriz de confusión para evaluar el rendimiento
  fig, ax = plt.subplots(figsize=(5, 4))
  sns.heatmap(
      matriz,
      annot=True,
      fmt="d",
      cmap="Blues",
      xticklabels=["Retenido(0)", "Abandono(1)"],
      yticklabels=["Retenido(0)", "Abandono(1)"],
      ax=ax,
  )
  ax.set_title("Matriz de Confusión")
  ax.set_xlabel("Predicción")
  ax.set_ylabel("Realidad")
  plt.tight_layout()

  # Devolvemos todo para la interfaz de Streamlit
  return df_clientes, modelo_churn, scaler, fig, accuracy, precision, recall