""" LOOPS """


""" FOR """
# Se genera una variable interna en el loop for
nombres = ["Horacio", "Alejandra", "Kmi"]

for nombre in nombres:
    print(f"Hola {nombre}")
print("\n")

#Statswith verifica si el string es la letra pasada por parametro
for nombre in nombres:
    if nombre.startswith('l'):
        print('Tu nombre comienza con L')
    else:
        print('No comienza con L')
print("\n")


numeros = [1, 2, 3]
resultado = 0

# Funcionamiento con numeros igual a la de javascript
# Tener cuidado con el nivel y la posicion del tap.
for numero in numeros:
    resultado = resultado + numero

print(resultado)
print("\n")

""" IMPORTANTEEEEE """

# Iteracion anidada

# Para hacerlo colocar multiplos valores.
# Respetar el numero de valores existentes.
# No es recomendable.
for a,b in [[1, 2], [3, 4]]:
    print(a)
    print(b)
print("\n")


# Iteracion en diccionario

dic = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}


for obj in dic.items():
    print(obj)
print("\n")



""" WHILE """
# Se ejecuta mientras la condicion sea verdadero

monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas = monedas - 1
# Se puede añadir else para que se ejecute cuando acabe el loop del while
else:
    print(f"No tengo mas monedas")
print("\n")
    

# Ejemplo con input del usuario
respuesta = 'y'

while respuesta == 'y':
    respuesta = input('Quieres seguir? (n / y) ')
else:
    print('Gracias por acabar conmigo')
print("\n")



""" RANGO / RANGE """
# Nos permite colocar un rango de ejecucion de un loop

for n in range(10):
    print(n)
print("\n")


# Se puede agregar a range parametros para el inicio, el final y la intermediacion.


for n in range(10, 20, 2):
    print(n)
print("\n")

#Crear listas de forma rapida.

lista = list(range(1, 100))




""" ENUMERADOR / ENUMERATE """
# Nos permite enumerar los indices de una lista

lista = ["a", "b", "c"]

for letra in enumerate(lista):
    print(letra)
print("\n")

# Agregando multiple variable en el for obtendremos los numeros por separado.
# La variable que contiene el numero es el primero qeu se pasa.

for i, letra in enumerate(lista):
    print(i, letra)
print("\n")













