""" Ejercicio 1 """

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
    print(f"Hola {alumno}")


""" Ejercicio 2 """

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for n in lista_numeros:
    suma_numeros = suma_numeros + n

print(suma_numeros)


""" Ejercicio 3 """

suma_pares = 0
suma_impares = 0


for n in lista_numeros:
    if n % 2 == 0: 
        suma_pares = suma_pares + n
    else :
        suma_impares = suma_impares + n

print(suma_pares)
print(suma_impares)



