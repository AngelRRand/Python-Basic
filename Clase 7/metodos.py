""" Ejercicio 1 """
print("\n")
class Perro:
    def ladrar():
        print("Guau")

mi_perro = Perro

mi_perro.ladrar()

""" Ejercicio 2 """
print("\n")

class Mago:
    def lanzar_hechizo():
        print("¡Abracadabra!")

merlin = Mago

merlin.lanzar_hechizo()


""" Ejercicio 3 """
print("\n")

class Alarma:
    def postergar(self, minutos):
        print(f"La alarma ha sido pospuesta {minutos} minutos")

mi_alarma = Alarma()


mi_alarma.postergar(10)