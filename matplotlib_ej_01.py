import matplotlib.pyplot as plt
import pandas as pd

datos = {
    "Precios": [1200, 1500, 1800, 2000, 2500],
    "Metros_cuadrados": [22,21,40, 80, 110],
    "Recamaras": [2,2,2,3,4]
}

df = pd.DataFrame(datos)

plt.figure()
plt.plot(df["Metros_cuadrados"], df["Precios"])
plt.xlabel("Metros Cuadrados")
plt.ylabel("Precio (miles de pesos)")
plt.title("Relacion entre precio y tamaño de la vivienad")
plt.show()