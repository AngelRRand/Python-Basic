""" Ejercicio 1 """
print("\n")
class Casa:
    

    def __init__(self, color, cantidad_pisos):

        self.color = color
        self.cantidad_pisos = cantidad_pisos
        pass

casa_blanca = Casa("Blanco", 4)

print(casa_blanca.cantidad_pisos)

""" Ejercicio 2 """
print("\n")

class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo("rojo")

print(f"Mi cubo tiene {cubo_rojo.caras} y es de color {cubo_rojo.color}")


""" Ejercicio 3 """
print("\n")


estado = {False: "no es real", True: "es real"}

class Personaje:
    real = False

    def __init__(self, especie, magia, edad):
        self.especie = especie
        self.magia = magia
        self.edad = edad
    

harry_potter = Personaje("Humano", True, 17)

print(f"Mi personaje es un {harry_potter.especie} tiene {harry_potter.edad} y {estado[harry_potter.real]}")
