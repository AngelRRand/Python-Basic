from collections import defaultdict
from collections import Counter

""" Ejercicio 1 """
print("\n")
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)

print(contador)

""" Ejercicio 2 """
print("\n")



mi_diccionario = defaultdict(lambda: "No encontrado")
mi_diccionario["edad"]  = 44
print(mi_diccionario["nombre"])

print(mi_diccionario)

""" Ejercicio 3 """
print("\n")
