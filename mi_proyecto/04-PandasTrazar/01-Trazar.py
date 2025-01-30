'''
Trazar
Pandas usa el plot() método para crear diagramas.
Podemos utilizar Pyplot, un submódulo de la biblioteca Matplotlib
para visualizar el diagrama en la pantalla.
'''

# Importe pyplot desde Matplotlib y visualice nuestro DataFrame:
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

'''
Parcela de Dispersión
Especifique que desea un gráfico de dispersión con el kind argumento:
kind = "scatter"
Un gráfico de dispersión necesita un eje x y un eje y.
En el siguiente ejemplo usaremos "Duración" para el eje x y "Calorías" para el eje y.
Incluye los argumentos x e y como este:
x = "Duration", y = "Calories"
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()

# Un diagrama de dispersión donde no hay relación entre las columnas:
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()

'''
Histograma
Usa el kind argumento para especificar que desea un histograma:
kind = 'hist'
Un histograma necesita solo una columna.
Un histograma nos muestra la frecuencia de cada intervalo,
por ejemplo, ¿cuántos entrenamientos duraron entre 50 y 60 minutos?
En el siguiente ejemplo, usaremos la columna "Duración"
para crear el histograma:
'''

# Ejemplo
df["Duration"].plot(kind = 'hist')

