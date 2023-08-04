""" Ejercicio 1 """
print("\n")

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')



""" Ejercicio 2 """
print("\n")

lista_indices = list(enumerate("python"))
print(lista_indices)


""" Ejercicio 3 """
print("\n")


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for i, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(i)