""" Ejercicio 1 """
print("\n")

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return f"{self.titulo}, de {self.autor}"
    
    def __len__(self):
        return self.cantidad_paginas
    
    def __del__(self):
        print("Libro eliminado")

mi_libro = Libro("Vida de mierda", "Orasio", 1)

print(mi_libro)

""" Ejercicio 2 """
print("\n")

print(len(mi_libro))

""" Ejercicio 3 """
print("\n")

del mi_libro
