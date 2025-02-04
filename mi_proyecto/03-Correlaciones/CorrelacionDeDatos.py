'''
Encontrar Relaciones
Un gran aspecto del módulo Pandas es el corr() método.
El corr() el método calcula la relación entre cada columna en su conjunto de datos.
Los ejemplos de esta página usan un archivo CSV llamado: 'data.csv'.
'''

# Mostrar la relación entre las columnas:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.corr())

'''
Correlación Perfecta:
Podemos ver que "Duración" y "Duración" obtuvieron el número 1.000000,
lo que tiene sentido cada columna siempre tiene una relación perfecta consigo misma.
Buena Correlación:
"Duración" y "Calorías" tienen un 0.922721 correlación, lo cual es una muy buena
correlación, y podemos predecir que cuanto más tiempo trabaje fuera, cuantas más
calorías queme, y al revés: si quemó mucho de calorías, probablemente tuviste un largo ejercicio.
Mala Correlación:
"Duración" y "Maxpulse" tiene un 0.009403 correlación, lo cual es una correlación
muy mala, lo que significa que no podemos predecir el pulso máximo con solo mirar
la duración del ejercicio, y viceversa.
'''
