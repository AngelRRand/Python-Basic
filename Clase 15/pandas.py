# Importamos Pandas
import pandas as pd


# Creamos una serie de números y hallamos su media
numeros = pd.Series([1,2,3,4,5,6,77])
numeros.mean()


# Hallamos la suma de dichos números
numeros.sum()


# Creamos una SERIE de tres colores diferentes
colores = pd.Series(["rojo", "amarillo", "verde"])


# Visualizamos la serie creada
colores


# Creamos una serie con tipos de autos, y la visualizamos
tipos_autos = pd.Series(["sedan", "SUV", "Pick"])
tipos_autos



# Combinamos las series de tipos de autos y colores en un DATAFRAME
tabla_autos = pd.DataFrame({"Tipo de auto": tipos_autos, "Color": colores})
tabla_autos


""" 
from google.colab import drive
drive.mount("/content/drive")
 """
# Importar "ventas-autos.csv" y convertirlo en un nuevo DATAFRAME
ventas_autos = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/ventas-autos.csv')
ventas_autos

# Exportar el Dataframe como un archivo CSV a mi carpeta "/content/drive/MyDrive/Colab Notebooks/pruebas/"
ventas_autos.to_csv("/content/drive/MyDrive/Colab Notebooks/pruebas/este_archivo.csv")

# Analicemos los tipos de datos disponibles en el dataset de ventas autos
ventas_autos.dtypes

# Apliquemos estadística descriptiva (cantidad de valores, media, desviación estándar, valores mínimos y máximos, cuartiles) al dataset
ventas_autos.describe()

# Obtenemos información del dataset utilizando info()
ventas_autos.info()

# Listamos los nombres de las columnas de nuestro dataset
ventas_autos.columns

# Averiguamos el "largo" de nuestro dataset
len(ventas_autos)

# Mostramos las primeras 5 filas del dataset
ventas_autos.head()

# Mostramos las primeras 7 filas del dataset
ventas_autos.head(7)

# Mostramos las últimas 5 filas del dataset
ventas_autos.tail(5)

# Utilizamos .loc para seleccionar la fila de índice 3 del DataFrame
ventas_autos.loc[3]

# Utilizamos .iloc para seleccionar las filas 3, 7 y 9
ventas_autos.iloc[[3,7,9]]

# Seleccionar la columna "Kilometraje"
ventas_autos['Kilometraje']

# Encontrar el valor medio de la columnas "Kilometraje"
ventas_autos['Kilometraje'].mean()

# Seleccionar aquellas columnas que tengan valores superiores a 100,000 kilómetros en la columna Kilometraje
ventas_autos[ventas_autos['Kilometraje'] > 100000]

# Creamos una tabla cruzada de doble entrada entre Fabricante y cantidad de puertas
pd.crosstab(ventas_autos['Fabricante'], ventas_autos['Puertas'])

# Agrupamos las columnas por fabricante y buscandos el valor medio de las columnas numéricas
ventas_autos.groupby(['Fabricante']).mean()

