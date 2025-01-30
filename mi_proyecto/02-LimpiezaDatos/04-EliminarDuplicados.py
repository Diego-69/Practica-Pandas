'''
Descubriendo Duplicados
Las filas duplicadas son filas que se han registrado más de una vez.
'''

# Devoluciones True por cada fila que es un duplicado, de otra manera False:
import pandas as pd

df = pd.read_csv('data.csv')

print(df.duplicated())

# Eliminar todos los duplicados:
df = pd.read_csv('data.csv')

df.drop_duplicates(inplace = True)

print(df.to_string())



