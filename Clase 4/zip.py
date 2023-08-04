""" Ejercicio 1 """
print("\n")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

lista = list(zip(capitales, paises))

for capital, pais in lista:
    print(f"La capital de {pais} es {capital}")


""" Ejercicio 2 """
print("\n")

marcas = ["Orasio.it", "Vida de mierda", "Python"]
productos = ["Computadora", "yo", "Programando"]

mi_zip = list(zip(marcas, productos))
print(mi_zip)

""" Ejercicio 3 """
print("\n")

numero1 = ["uno", "um", "one"]
numero2 = ["dos", "dois", "two"]
numero3 = ["tres", "três", "three"]
numero4 = ["cuatro", "quatro", "four"]
numero5 = ["cinco", "cinco", "five"]

numeros = list(zip(numero1, numero2, numero3, numero4, numero5))
print(numeros)