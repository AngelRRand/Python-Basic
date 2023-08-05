""" Generar una lista de palabras """
""" Que la aplicacion elija 1 alazar """
""" Enseñar de alguna forma la cantidad de palabras que tiene la palabra elegida por la app """
""" Crear una funcion """
""" Que nos pida una letra. """
""" Validar la letra y ensañar todas las que coinciden con la palabra. """
"""  """
from random import *

palabras_españolas = [
    "hola",
    "amigo",
    "bienvenido",
    "gracias",
    "por",
    "favor",
    "manzana",
    "perro",
    "gato",
    "amor",
    "libro",
    "música",
    "comida",
    "agua",
    "familia",
    "casa",
    "escuela",
    "trabajo",
    "jugar",
    "correr",
    "caminar",
    "ciudad",
    "campo",
    "montaña",
    "mar",
    "sol",
    "luna",
    "estrella",
    "cielo",
    "tierra",
    "planta",
    "flor",
    "árbol",
    "bosque",
    "río",
    "lago",
    "oceano",
    "nube",
    "lluvia",
    "nieve",
    "hielo",
    "fuego",
    "viento",
    "aire",
    "humo",
    "piedra",
    "metal",
    "madera",
    "papel",
    "tijera",
    "boli",
    "lápiz",
    "libreta",
    "mesa",
    "silla",
    "sofá",
    "cama",
    "puerta",
    "ventana",
    "techo",
    "pared",
    "suelo",
    "escalera",
    "coche",
    "bicicleta",
    "avión",
    "tren",
    "barco",
    "calle",
    "carretera",
    "puente",
    "túnel",
    "semáforo",
    "farola",
    "edificio",
    "torre",
    "iglesia",
    "castillo",
    "palacio",
    "museo",
    "biblioteca",
    "parque",
    "jardín",
    "bosque",
    "desierto",
    "playa",
    "isla",
    "continente",
    "oceanía",
    "europa",
    "américa",
    "áfrica",
    "asia",
    "antártida",
]


palabra_alazar = choice(palabras_españolas)
letras_usuario = []
vidas = 6

print("\n")
print(palabra_alazar)

print("Bienvenido! Vamos a jugar al ahorcado.")

print("\n")
print("COMENCEMOS")
print("\n")

def inicio_ronda(vidas, letras_usuario, palabra_alazar):

    while vidas > 0:
        vidas -= 1

        letra = input(f'Tienes {vidas} intentos. Dime una letra: ').lower()

        validar_letra(letra, letras_usuario)

        dibujo_print(letras_usuario, palabra_alazar)

        if(validar_victoria(letras_usuario, palabra_alazar)):
            print("Haz ganado felicidades!!!!")
            break

        print("\n")

    else:
        print(f"Has perdido la palabra era {palabra_alazar}")


def dibujo_print(letras_usuario, palabra_alazar):
    muestra = []
    for p in palabra_alazar:
        if p in letras_usuario:
            muestra.append(p)
        else:
            muestra.append("_")
    resultado = " ".join(muestra)
    print("\n")
    print(resultado)
    print("\n")

def validar_letra(letra, letras_usuario):

    while len(letra) >= 2 or letra.isdigit() or len(letra) == 0 or letra in letras_usuario:
        if letra.isdigit(): 
            letra = input('Solo puede ingresar letras. \nDime una letra: ')
        elif len(letra) == 0:
            letra = input('No has ingresado nada...\nDime una letra: ')
        elif letra in letras_usuario:
            letra = input('Esa letra ya fue ingresada antes.\nDime una letra: ')
        else:
            letra = input('Solo puede ingresar una letra por intento. \nDime una letra: ')
    else:
        letras_usuario.append(letra)
        return

def validar_victoria(letras_usuario, palabra_alazar):
    palabra_formada = ""
    for p in palabra_alazar:
        for a in letras_usuario:
            if p.startswith(a):
                palabra_formada += p
    if palabra_alazar == palabra_formada:
        return True
    else:
        return False
    
        

inicio_ronda(vidas, letras_usuario, palabra_alazar)
print("\n")