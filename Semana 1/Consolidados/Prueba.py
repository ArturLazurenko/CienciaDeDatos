import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

print("Todo funciona correctamente")

# Ejemplo simple
x = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

modelo = LinearRegression()
modelo.fit(x, y)

print("Predicción para 5:", modelo.predict([[5]]))