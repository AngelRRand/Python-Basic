""" Ejercicio 1 """
print("\n")

lis = list(range(-1, 10))

def todos_positivos(lista):
    for n in lista:
        if n < 0:
            return False
    return True


print(todos_positivos(lis))



""" Ejercicio 2 """
print("\n")


lista_numeros = list(range(1, 2000))
def suma_menores(lista):
    suma = 0
    for n in lista:
        if (n > 0) and (n < 1000):
            suma += n
    return suma

print(suma_menores(lista_numeros))



""" Ejercicio 3 """
print("\n")


lista_numeros = list(range(1, 10))

def cantidad_pares(lista):
    count = 0
    for n in lista:
        if n % 2 == 0:
            count += 1
    return count

print(cantidad_pares(lista_numeros))


