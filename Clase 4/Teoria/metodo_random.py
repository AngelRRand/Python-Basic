""" IMPORTACION DE LIBRERIAS Y METODOS DE ESTAS """


from random import *

# randint
# Entrega un numero aleatorio entre los numeros que pongamos en los parametros.

aleatorio = randint(1, 50)
print(aleatorio)

print("\n")

# uniform
# Entrega un numero aleatorio entre los numeros que pongamos en los parametros.
# Con valores decimales.

aleatorio = uniform(1, 50)
print(aleatorio)

print("\n")


# random
# Entrega un numero aleatorio entre 0 y 1.
# Con valores decimales.

aleatorio = random()
print(aleatorio)

print("\n")


# choice
# Entrega un valor random de una lista

colores = ["azul", "rojo", "amarillo"]
aleatorio = choice(colores)
print(aleatorio)

print("\n")



# choice
# Desordena de forma aleatria una lista

numeros = list(range(0, 51))
shuffle(numeros)

print(numeros)