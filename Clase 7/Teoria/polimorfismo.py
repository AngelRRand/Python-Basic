""" Polimorfismo """


class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre
        pass
    def hablar(self):
        print(f"la {self.nombre} dice muuuuu")



class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre
        pass
    def hablar(self):
        print(f"la {self.nombre} dice beeee")

print("\n")

# Llamar a los metodos con el mismo nombre 
vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")

vaca1.hablar()
oveja1.hablar()

print("\n")

# Iteracion
animales = [vaca1, oveja1]

for animal in animales :
    animal.hablar()

print("\n")

# Funciones
def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)
    

