# leer un archivo csv
import pandas as pd

df = pd.read_csv("Practica-Pandas/mi_proyecto/data.csv")

# imprime todo el dataframe
print(df.to_string())

# omprime los primero 5 registros y los ultimo 5 registros
print(df)

# imprime el numero de filas
print(pd.options.display.max_rows) 