from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score

x_train = [[5], [4], [6], [7], [3], [1], [0]]
y_train = [1, 1, 1, 1, 1, 0, 0]

modelo = LogisticRegression()
modelo.fit(x_train, y_train)


x_test = [[2], [1], [4]]
y_test = [0, 0, 1]

#Predicciones

y_pred = modelo.predict(x_test)

print("Predicciones: ", precision_score(y_test, y_pred))
print("recall: ", recall_score(y_test, y_pred))
print("f1: ", f1_score(y_test, y_pred))