import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from conexion import engine, query


def cargar_y_entrenar_modelo():
  # 1. Extraer datos de SQL Server
  df_clientes = pd.read_sql(query, engine) # Leemos la conexion y ejecutamos la consulta(desde conexion.py) y la convertimos en un DataFrame de pandas
  print("--- DATOS EXTRAÍDOS DE SQL SERVER ---")
  print(df_clientes.head())

  # 2. Revisar los clientes que tengan más de 2 devoluciones o menos de 10 minutos en la tienda y marcarlos como churn (1) o no churn (0)
  df_clientes["churn"] = np.where( # Se crea la columna churn y agreegamos un condicinal de numpy para marcar a los clientes que cumplen con la condición de riesgo de fuga
      (df_clientes["devoluciones"] >= 2) | (df_clientes["tiempo_en_tienda"] < 10), # Condición: si el cliente tiene 2 o más devoluciones o ha pasado menos de 10 minutos en la tienda
      1, # valores asignado si cumple la condición (churn)
      0,
  )

  x = df_clientes[["tiempo_en_tienda", "cantidad_compras", "devoluciones"]] # Separamos las variables predictoras (X) de la variable objetivo (y)
  y = df_clientes["churn"] # Guardamos la variable objetivo (y) que indica si el cliente es churn o no

  # 3. Dividir datos y entrenar
  X_train, X_test, y_train, y_test = train_test_split( # Separamos los datos en conjunto de entrenamiento y prueba
      x, y, test_size=0.2, random_state=42 # Separamos el 20% de los datos para prueba y el 80% para entrenamiento, con una semilla aleatoria para reproducibilidad
  )

  scaler = StandardScaler() # Creamos un objeto StandardScaler para normalizar los datos
  x_train_scaled = scaler.fit_transform(X_train) # Ajustamos el scaler a los datos de entrenamiento y transformamos los datos de entrenamiento
  X_test_scaled = scaler.transform(X_test) # Transformamos los datos de prueba usando el mismo scaler ajustado a los datos de entrenamiento

  modelo_churn = LogisticRegression() # Creamos un objeto LogisticRegression para entrenar el modelo de regresión logística
  modelo_churn.fit(x_train_scaled, y_train) # Entrenamos el modelo con los datos de entrenamiento escalados y la variable objetivo

  # Devolvemos lo necesario para la interfaz de Streamlit
  return df_clientes, modelo_churn, scaler