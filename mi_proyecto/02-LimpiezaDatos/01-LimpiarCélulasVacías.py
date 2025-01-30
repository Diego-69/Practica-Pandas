'''
Limpieza de Datos
La limpieza de datos significa arreglar datos incorrectos en su conjunto de datos.
Los datos malos podrían ser:
Células vacías
Datos en formato incorrecto
Datos incorrectos
Duplicados
'''

'''
Células Vacías
Las células vacías pueden potencialmente darle un resultado incorrecto cuando analiza datos.
imprime todo sin celdas vacias
'''
# Devuelve un nuevo Marco de datos sin celdas vacías:
import pandas as pd

df = pd.read_csv('mi_proyecto/data.csv')

new_df = df.dropna()

print(new_df.to_string())

# Eliminar todas las filas con valores NULL:
df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())

# Reemplace los valores NULL con el número 130:
df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)

# Reemplace los valores NULL en las columnas "Calorías" con el número 130:
df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True)

# Calcule el MEAN y reemplace cualquier valor vacío con él:
df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

# Calcule el MEDIAN y reemplace cualquier valor vacío con él:
df = pd.read_csv('data.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)

# Calcule el MODO y reemplace cualquier valor vacío con él:
df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)




