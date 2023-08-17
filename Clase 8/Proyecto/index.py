from os import system
from Paquete import turnos


mensaje = """
Diga para que area desea sacar su turno.

1 - Perfume
2 - Farmacia
3 - Cosmetica
4 - Salir
"""
system("cls")
""" nombre = input("Bienvenido, dime ¿Como te llamas? ") """


def ejecutar():
    perfume = turnos.generar_turno("P")
    cosmetico = turnos.generar_turno("C")
    farmacia = turnos.generar_turno("F")
    while True:
        respuesta = validar_opcion()
        match respuesta:
            case 1:
                print(f"Tu turno es {next(perfume)} aguarde")
            case 2:
                print(f"Tu turno es {next(farmacia)} aguarde")
            case 3:
                print(f"Tu turno es {next(cosmetico)} aguarde")
            case 4:
                return


def validar_opcion():
    while True:
        try:
            """ system("cls") """
            print(mensaje)
            opcion = int(input("Que quieres hacer? "))
        except:
            print("Tu opcion no es valida.")
        else:
            return opcion


ejecutar()
