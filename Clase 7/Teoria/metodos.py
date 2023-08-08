
""" PROGRAMACION ORIENTADA A OBJETOS """

# Se define con class seguido de un nombre en mayuscula

# Init hace un metodo constructor.
# Se da una instancia de la clase con self o "si mismo"
# Metodos se usan con la palabra def
class Pajaro:
    alas = True
    def __init__(self, color, especie) :

        self.color = color
        self.especie = especie

    def piar(self):
        print(f"pio")

    # Metodos de instancia

    # Pueden acceder a los atributos del objeto
    # Pueden acceder a otros metodos
    # Pueden modificar el estado de la clase
    def volar(self, metros):
        print(f"tu pajaro ha volado {metros} metros")
        self.piar()
    
    def pintarlo(self):
        self.color = "rojo"
        print(f"Ahora su color es {self.color}")


    # Metodos de clase
    # No necesitan instancia para ejecutarse
    # No pueden acceder a los atributos de instancia
    # Si pueden acceder a los atributos de de clase

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")


    # Metodos estaticos
    # No pueden acceder a los atributos de instancia
    # No pueden acceder a los atributos de de clase
    
    @staticmethod
    def mirar():
        print("El pajaro mira")


    
# No es posible usar un metodo de instancia sin una instancia previa
#Pajaro.piar()

# Solo es posible con los metodos de clase
Pajaro.poner_huevos(5) 

Pajaro.mirar()

mi_pajaro = Pajaro("negro", "cuervo")

print(f"mi pajaro es un {mi_pajaro.especie} de color {mi_pajaro.color}")

mi_pajaro.piar()
mi_pajaro.volar(50)
mi_pajaro.pintarlo()

