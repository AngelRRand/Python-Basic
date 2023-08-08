""" HERENCIA """

class Animal:
    
    def __init__(self, edad, color) :
        self.edad = edad
        self.color = color
        pass


    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")



# La herencia se hace de una clase a otra colacando los parentesis
# Seguido del nombre de la clase que esta heredando.

class Pajaro(Animal):

    #Se puede añadir atributos de instancia
    def __init__(self, edad, color, altura_vuelo) :
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    #Se puede modificar los metodos heredados
    def hablar(self):
        print("Pio")
    
    #Se puede metodos
    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")




piolin = Pajaro(2, "amarillo", 40)

piolin.nacer()

print(piolin.color)

piolin.hablar()




print("\n")





""" HERENCIA MULTIPLE """

class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("JAJA")

    def hablar(self):
        print("Que tal")

# Depende del orden en el que se fue heredando
# Siendo los primero los que tienen prioridad
class Hijo(Madre, Padre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()

mi_nieto.hablar()
mi_nieto.reir()





print("\n")

