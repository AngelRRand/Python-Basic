""" Ejercicio 1 """
print("\n")


class Mascota:

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")



Mascota.respirar()

""" Ejercicio 2 """
print("\n")

class Jugador:

    vivo = False


    @classmethod
    def revivir(cls):
        cls.vivo = True
        print(f"El valor de vivo es: {cls.vivo}")


Jugador.revivir()

""" Ejercicio 3 """
print("\n")

class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1
        print(f"La cantidad de flechas que tienes es {self.cantidad_flechas}")


mi_personaje = Personaje(10)

mi_personaje.lanzar_flecha()
mi_personaje.lanzar_flecha()
mi_personaje.lanzar_flecha()
mi_personaje.lanzar_flecha()
mi_personaje.lanzar_flecha()
mi_personaje.lanzar_flecha()
mi_personaje.lanzar_flecha()
mi_personaje.lanzar_flecha()