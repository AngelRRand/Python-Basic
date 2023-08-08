print("OPP")

# Se define con class seguido de un nombre en mayuscula

# Init hace un metodo constructor.
# Se da una instancia de la clase con self o "si mismo"
class Pajaro:
    def __init__(self, color) :

        self.color = color
        pass



cuervo = Pajaro("negro")

print(cuervo.color)