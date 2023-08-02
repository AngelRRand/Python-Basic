""" METODOS STRING """

texto = "Controlar la complejidad es la esencia de la programación"

a = "Aprender"
b = "Python"


""" UPPER """
# Convertir todo en mayuscula
# CONTROLAR LA COMPLEJIDAD ES LA ESENCIA DE LA PROGRAMACIÓN
print(texto.upper())

""" LOWER """
# Convertir todo en minuscula
# controlar la complejidad es la esencia de la programación
print(texto.lower())


""" SPLIT """
# Separa todos las palabras en una lista
# ['Controlar', 'la', 'complejidad', 'es', 'la', 'esencia', 'de', 'la', 'programación']

print(texto.split())

# El separador se puede aclarar en el metodo
# ['Con', 'rolar la complejidad es la esencia de la programación']

print(texto.split("t"))

""" JOIN """
# Une las cadenas de texto, pudiendo modificar el separador.
# Aprender Python

print(" ".join([a,b]))

# Aprender-Python

print("-".join([a,b]))

""" FIND """
# Al igual que index encuentra la cadena buscada en el texto y te devuelve su posicion
# 1

print(texto.find("o"))

""" REPLACE """
# Remplasa la palabra encontrada con la sumanda.
# Cantralar la camplejidad es la esencia de la pragramación

print(texto.replace("o", "a"))

#ControLAr LA complejidad es LA esencia de LA programación

print(texto.replace("la", "LA"))