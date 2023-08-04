""" PRUEBA """
pies = [10,20,30,40,50]
metros = [ n / 3.281 for n in pies]

print(metros)


""" Ejercicio 1 """
print("\n")

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n ** 2 for n in valores]

print(valores_cuadrado)

""" Ejercicio 2 """
print("\n")

valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [n for n in valores if n % 2 == 0]

print(valores_pares)


""" Ejercicio 3 """
print("\n")

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(n - 32) * (5 / 9) for n in temperatura_fahrenheit]

print(grados_celsius)