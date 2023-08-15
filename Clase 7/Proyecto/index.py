from os import system
from random import *

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir_cliente(self):
        print(
            f"""
Bienvenido {self.nombre} {self.apellido}.
 _______________________________________________
-Tu numero de cuenta es: {self.numero_cuenta}
-Tu balance de cuenta es: {self.balance}   
 ________________________________________________
            """)

    def depositar(self, deposito):
        self.balance += deposito
        pass

    def retirar(self, retiro):
        self.balance -= retiro
        pass

def inicio():
    ejecutando = True 
    opcion = ""
    cliente = crear_cliente()
    while ejecutando:
        system("cls")
        cliente.imprimir_cliente()
        opcion = validar_opcion()
        
        print("\n")
        match opcion:
            case "depositar":
                system("cls")
                deposito = validar_cantidad_valores("deposito")
                cliente.depositar(deposito)
            case "retirar":
                system("cls")
                retirar = validar_cantidad_valores("retirar")
                while retirar > cliente.balance:
                    mensajes_consola(f"La cantidad solicitada excede tus fondos prueba con otro monto menor a {cliente.balance}")
                    retirar = validar_cantidad_valores("retirar")
                else:
                    cliente.retirar(retirar)
            case "salir":
                ejecutando = False
    else:
        system("cls")
        print("Ejecucion terminada") 


def crear_cliente():
    mensajes_consola("Bienvenido")
    nombre = validar_cuenta_valores("nombre")
    apellido = validar_cuenta_valores("apellido")
    numero_de_cuenta = randint(0, 99999999)
    cliente = Cliente(nombre, apellido, numero_de_cuenta, 10000)
    return cliente

def validar_cuenta_valores(clase):
        valor = input(f"Dime cual es tu {clase}: ")
        while valor.isdigit():
            mensajes_consola("No puedes ingresar este valor. Por favor vuelve a intentarlo")
            valor = input(f"Dime cual es tu {clase}: ")
        else:
            return valor

def validar_cantidad_valores(clase):
    valor = input(f"¿Cuanto quieres {clase} en tu cuenta? ")
    while valor.isdigit() == False:
        mensajes_consola("No puedes ingresar este valor. Por favor vuelve a intentarlo")
        valor = input(f"¿Cuanto quieres {clase} en tu cuenta? ")
    else:
        return int(valor)
        
def validar_opcion():
    opciones = ["depositar", "retirar", "salir"]
    mensaje = """     
1 - Depositar
2 - Retirar
3 - Salir   
¿Que deseas hacer? """
    opcion = input(mensaje)
    
    while opcion.lower() not in opciones:
        mensajes_consola("No puedes ingresar este valor. Por favor vuelve a intentarloooo")
        opcion = input(mensaje)
    else:
        return opcion.lower()

def mensajes_consola(mensaje):
    system("cls")
    print(f"""
________________________
{mensaje}
________________________
          """)
    


inicio()
