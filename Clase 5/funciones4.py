from random import *
""" Ejercicio 1 """
print("\n")

def lanzar_dados():
    return randint(1,6)

def evaluar_jugada():
    suma_dados = lanzar_dados() + lanzar_dados() 
    if (suma_dados <= 6):
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif (suma_dados > 6 and suma_dados < 10):
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")


evaluar_jugada()
""" Ejercicio 2 """
print("\n")


lista_numeros = [1,2,15,7,2,5,7] 
def reducir_lista(lis):
    new_lista = set(lis)
    max_value = max(new_lista)
    
    new_lista.discard(max_value)
    return new_lista

def promedio(lis):
    count = 0
    for n in lis:
        count += n
    return round(count / len(lis), 2)

resultado = promedio(reducir_lista(lista_numeros))

print(resultado)

""" Ejercicio 3 """
print("\n")

lista_numeros = list(range(1,10))

def lanzar_moneda():
    posibilidades = ["Cara", "Cruz"]
    resultado = choice(posibilidades)
    return resultado

def probar_suerte(moneda, lis):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        lis = []
    else:
        print("La lista fue salvada")
    return lis

probar_suerte(lanzar_moneda(), lista_numeros)