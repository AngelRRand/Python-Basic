""" FUNCIONES GENERADORAS """

# Entrega siempre el siguiente dato que se le pida



def mi_funcion():
    return 4

def mi_generador():
    yield 4



print(mi_funcion())
print(mi_generador())



#La forma de ejecutar una funcion generadora es con el next
print(next(mi_generador()))

def mi_funcion2():
    lista = []
    for n in range(1,5):
        lista.append(n * 10)

    return lista

print(mi_funcion2())

def mi_generador2():
    for n in range(1,5):
        yield n * 10

print(next(mi_generador2())) #Entrega 10
print(next(mi_generador2())) #Entrega 10
print(next(mi_generador2())) #Entrega 10

a = mi_generador2()

print(next(a)) #Entrega 10
print(next(a)) #Entrega 20
print(next(a)) #Entrega 30