""" Ejercicio 1 """
import math

print("\n")


def numero_infinito():
    n = 1
    while True:
        yield n
        n += 1


generador = numero_infinito()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))


""" Ejercicio 2 """
print("\n")


def muntiplo_siete_infinito():
    m = 1
    n = 7
    while True:
        yield n * m
        m += 1


generador2 = muntiplo_siete_infinito()

print(next(generador2))
print(next(generador2))
print(next(generador2))
print(next(generador2))
print(next(generador2))
print(next(generador2))
print(next(generador2))


""" Ejercicio 3 """
print("\n")


def perder_vidas():
    yield "Te quedan 3 vidas"
    yield "Te quedan 2 vidas"
    yield "Te quedan 1 vidas"
    yield "Game Over"


generador3 = perder_vidas()

print(next(generador3))
print(next(generador3))
print(next(generador3))
print(next(generador3))
