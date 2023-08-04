""" Ejercicio 1 """
print("\n")

def suma_cuadrados(*args):
    count = 0
    for n in args:
        count += n ** 2
    return count

print(suma_cuadrados(1, 2, 3))

""" Ejercicio 2 """
print("\n")

def suma_absolutos(*args):
    count = 0
    for n in args:
        count += abs(n)
    return count

print(suma_absolutos(1, 2, -3))




""" Ejercicio 3 """
print("\n")

def numeros_persona (nombre, *args):
    print(f"{nombre}, la suma de tus números es {sum(args)}")
    
numeros_persona("Horacio", 1, 2, 3, 90)