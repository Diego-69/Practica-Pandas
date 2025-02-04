'''
Ver los Datos
Uno de los métodos más utilizados para obtener una visión general
rápida del DataFrame, es el head() método.
El head() el método devuelve los encabezados y un número
específico de filas, comenzando desde la parte superior.
'''

# uso del head() para ver los primeros 10 registros de un archivo csv

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))

# imprimir los primeros 5 registros

df = pd.read_csv('data.csv')

print(df.head())

# imprime las 5 ultimas filas

df = pd.read_csv('data.csv')

print(df.tail())

# imprime la informacion de los datos

df = pd.read_csv('data.csv')

print(df.info())