'''
Datos Equivocados
"Datos incorrectos" no tiene que ser "celdas vacías" o "formato incorrecto",
puede solo equívoco, como si alguien registrara "199" en lugar de "1.99".
A veces puede detectar datos incorrectos mirando el conjunto de datos,
porque tiene una expectativa de qué debería ser.
Si echa un vistazo a nuestro conjunto de datos,
puede ver que en la fila 7, la duración es de 45,
pero para todas las demás filas la duración es de entre 30 y 60.
No tiene que estar mal, pero teniendo en cuenta que este es el conjunto
de datos del entrenamiento de alguien sesiones, concluimos con el hecho
de que esta persona no funcionó en 450 minutos.
'''

# Establecer "Duración" = 45 en la fila 7:
import pandas as pd

df = pd.read_csv('data.csv')

df.loc[7,'Duration'] = 45

print(df.to_string())

# Recorre todos los valores en la columna "Duración".
# Si el valor es superior a 120, establezca en 120:

df = pd.read_csv('data.csv')

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

print(df.to_string())

# Eliminar filas donde "Duración" es superior a 120:

df = pd.read_csv('data.csv')

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

print(df.to_string())


