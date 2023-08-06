from pathlib import Path
from os import system

system("cls")

""" Ejercicio 1 """
print("\n")

ruta_base = "C:/Users/Horac/OneDrive/Escritorio/Orasio/Aprendiendo/11 Aprendiendo Python/Python Basic/Clase 6/texto/funciones"


def abrir_leer(base):

    ruta = Path(base, "open.txt")

    return ruta.read_text() 


print(abrir_leer(ruta_base))


""" Ejercicio 2 """
print("\n")

def sobrescribir(base, archivo):
    directorio = Path(base, archivo)
    ruta = open(directorio, "w")

    ruta.write("contenido eliminado")

    ruta.close()

    texto = directorio.read_text() 
    return texto 

print(sobrescribir(ruta_base, "open.txt"))



""" Ejercicio 3 """
print("\n")


def registro_error(base, archivo):
    directorio = Path(base, archivo)
    with open(directorio, "a") as ruta:
        ruta.write("\nSe a encontrado un error")
    texto = directorio.read_text() 
    return texto 


print(registro_error(ruta_base, "open.txt"))

