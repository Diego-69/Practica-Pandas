# dataframe
import pandas as pd

# esto es un ejemplo de un dataframe con dos columnas

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)

print(type(data))