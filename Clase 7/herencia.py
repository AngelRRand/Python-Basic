""" Ejercicio 1 """
print("\n")

class Persona:


    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad




class Alumno(Persona):
    pass

primer_alumno = Alumno("Horisio", 23)

print(primer_alumno.nombre)
print(primer_alumno.edad)


""" Ejercicio 2 """
print("\n")


class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas


class Perro(Mascota):
    pass

mi_perro = Perro(10, "Tom", 4)
print(f"Mi perro se llama {mi_perro.nombre} y tiene {mi_perro.cantidad_patas} patas ")



""" Ejercicio 3 """
print("\n")


class Vehiculo:
    def acelerar(self):
        pass

    def frenar(self):
        print("RUUUUUNN")
        pass

class Automovil(Vehiculo):
    pass


mi_auto = Automovil()

mi_auto.frenar()