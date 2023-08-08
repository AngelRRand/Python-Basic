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
        print(f"pio, mi color es {self.color}")

    def volar(self, metros):
        print(f"tu pajaro ha volado {metros} metros")




mi_pajaro = Pajaro("negro", "cuervo")

print(f"mi pajaro es un {mi_pajaro.especie} de color {mi_pajaro.color}")

mi_pajaro.piar()
mi_pajaro.volar(50)