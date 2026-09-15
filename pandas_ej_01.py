import pandas as pd

datos = {
    "Precios": [1200, 1500, 1800, 2000, 2500],
    "Metros_cuadrados": [22,21,40, 80, 110],
    "Recamaras": [2,2,2,3,4]
}

df = pd.DataFrame(datos)

print(df)
print("Precio Promedio: ", df["Precios"].mean())