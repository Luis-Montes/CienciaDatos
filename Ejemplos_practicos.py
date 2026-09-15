# Prediccion para saber si un cliente va a comprar o no un producto

import pandas as pd
from sklearn.linear_model import LogisticRegression
# 1 Metricas para evaluar aciertos(f1_score, precision_score, recall_score)
# 2 Herramienta para ver con claridad los aciertos y errores de nuestro modelo (confusion_matrix)
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score

# Preparar los datos
# x_train son los minutos en la web
# y_train es si el cliente compro o no el producto

# # Minutos en la web de 8 usuarios:
# X_train = [[1], [2], [2], [3], [5], [6], [8], [9]]

# # 0 = No compró, 1 = Compró
# y_train = [0, 0, 0, 0, 1, 1, 1, 1]

# # Crear y entrenar el modelo
# # .fit() es el metodo que traza la curva de aprendizaje y ajusta el modelo a los datos

# modelo = LogisticRegression()
# modelo.fit(X_train, y_train)

# # Probar con datos nuevos

# # Nuevos visitantes: 2 min, 4 min, 7 min, 10 min
# X_test = [[2], [4], [7], [10]]

# # Lo que realmente hicieron en la vida real:
# # El de 4 min al final NO compró (0)
# y_test = [0, 0, 1, 1]

# # El modela hace predicciones con .predict()

# y_pred = modelo.predict(X_test)
# print("Lo que predijo el modelo:", y_pred)

# # Calcular y analizar las metricas de evaluacion
# print("Precisión:", precision_score(y_test, y_pred))
# print("Recall:", recall_score(y_test, y_pred))
# print("F1-Score:", f1_score(y_test, y_pred))


# x_train = [[1], [2], [3], [7], [8], [9]]
# y_train = [0, 0, 0, 1, 1, 1]

# modelo = LogisticRegression()
# modelo.fit(x_train, y_train)

# x_test = [[2], [4], [7], [10]]
# y_test = [0, 0, 1, 1]

# y_pred = modelo.predict(x_test)
# print("Lo que predijo el modelo:", y_pred)

# print("Precisión:", precision_score(y_test, y_pred))
# print("Recall:", recall_score(y_test, y_pred))
# print("F1-Score:", f1_score(y_test, y_pred))

df_2025 = pd.read_csv("clientes_2025.csv")

columnas_predictorias = ["Horas_mes", "Quejas_soporte", "Dias_inactivo"]
x_train = df_2025[columnas_predictorias]
y_train = df_2025["Cancelo"]

modelo = LogisticRegression()
modelo.fit(x_train, y_train)

df_2026 = pd.read_csv("clientes_2026.csv")
x_nuevo = df_2026[columnas_predictorias]

df_2026["cancela_predicho"] = modelo.predict(x_nuevo)
df_2026["Probabilidad_fuga_%"] = (
    modelo.predict_proba(x_nuevo)[:, 1] * 100
).round(2)

print(
    df_2026[
        [
            "Cliente_id",
            "Horas_mes",
            "Quejas_soporte",
            "Dias_inactivo",
            "cancela_predicho",
            "Probabilidad_fuga_%"
        ]
    ]
)