""" 
# Importar y preparar la librería
import matplotlib.pyplot as plt
%matplotlib inline
# Preparar los datos
x = list(range(101))
y = []
for n in x:
  y.append(n**2)

# Preparamos el área del gráfico (fig) y el gráfico en sí (ax) utilizando plt.subplots()
fig, ax = plt.subplots()

# Añadimos los datos al gráfico
ax.plot(x, y)

# Personalizamos el gráfico añadiendo título al gráfico y a los ejes x e y
ax.set(title= "Grafico de casos de COVID", xlabel= "dias", ylabel="casos confirmados")

# Guardamos nuestro gráfico empleando fig.savefig()
fig.savefig("/ejemplo.png")

#creamos un nuveo set de datos utilizando la librería Numpy
import numpy as np
x_1 = np.linspace(0, 100, 20)
print(x_1)
y_1 = x_1**2

# Creamos el gráfico de dispersión de x vs y
fig, ax = plt.subplots()
ax.scatter(x_1, y_1)

# Visualizamos ahora la función seno, utilizando np.sin(X)
fig, ax = plt.subplots()

x_2 = np.linspace(-10, 10, 100)
y_2 = np.sin(x_2)
print(x_2)
ax.scatter(x_2, y_2)



"""



""" 
# Creamos la misma disposición de gráficos, con un tamaño de figura de 10x5
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows = 2, ncols=2, figsize=(10, 5))

# Para nuestro primer gráfico, tomamos el conjunto x_1, y_1, y generamos un gráfico de líneas
ax1.plot(x_1, y_1)

# Para nuestro segundo gráfico, tomamos el conjunto x_2, y_2, y generamos un gráfico de dispersión
ax2.scatter(x_2, y_2)

# Creamos un gráfico con los precios de tres comidas en la esquina inferior izquierda
ax3.bar(comidas.keys(), comidas.values())

# El gráfico de la esquina inferior derecha será un histograma de valores aleatorios con distribución normal
ax4.hist(np.random.rand(1000))
 """