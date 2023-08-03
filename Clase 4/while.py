""" Ejercicio 1 """

numero = 10

while numero > 0:
    print(numero)
    numero -= 1


print("\n")
""" Ejercicio 2 """

numero = 50

while numero > 0:
    if numero % 5 == 0:
        print(numero)
    numero -= 1
    

print("\n")
""" Ejercicio 3 """

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]


for n in lista_numeros:
    if n < 0:
        break
    print(n)





