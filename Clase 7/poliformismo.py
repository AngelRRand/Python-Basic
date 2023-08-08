""" Ejercicio 1 """
print("\n")

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

class Iterar:
    def contar(self, dato):
        a = len(dato)
        return a
    

cantidad_letras = Iterar()
print(cantidad_letras.contar(palabra))
cantidad_datos = Iterar()
print(cantidad_datos.contar(lista))
cantidad_numeros = Iterar()
print(cantidad_numeros.contar(tupla))

print("\n")

for n in [palabra, lista, tupla]:
    print(len(n))

""" Ejercicio 2 """
print("\n")


class Mago():
    def atacar(self):
        print("Ataque mágico")
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")
    def defender(self):
        print("Esconderse")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
    def defender(self):
        print("Bloqueo")

mago = Mago()
arquero = Arquero()
samurai = Samurai()
personajes = [arquero, mago, samurai]

for p in personajes:
    p.atacar()



""" Ejercicio 3 """
print("\n")


def personaje_defender(personaje):
    personaje.defender()


personaje_defender(mago)
personaje_defender(arquero)
personaje_defender(samurai)