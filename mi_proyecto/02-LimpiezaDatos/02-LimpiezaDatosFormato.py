'''
Datos de Formato Incorrecto
Las celdas con datos de formato incorrecto pueden dificultar,
o incluso imposibilitar, el análisis de datos.
Para solucionarlo, tiene dos opciones: eliminar las filas o
convertir todas las celdas en el columnas en el mismo formato.
'''

# Convertir hasta la fecha:

import pandas as pd

df = pd.read_csv('mi_proyecto/data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())

'''
Remoción de Filas
El resultado de la conversión en el ejemplo anterior
nos dio un valor NaT, que se puede manejar
como un valor NULL, y podemos eliminar la fila
utilizando el dropna() método.
'''

# Eliminar filas con un valor NULL en la columna "Fecha":

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.dropna(subset=['Date'], inplace = True)

print(df.to_string())
