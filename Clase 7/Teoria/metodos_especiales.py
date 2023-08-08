""" METODOS ESPECIALES """

class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    # Modifica la forma en la que se va a ver el objeto.
    # Usar return
    def __str__(self):
        return f"{self.titulo} su autor es {self.autor}"
    
    # Devuelve la cantidad del valor que coloquemos
    def __len__(self):
        return self.canciones
    
    # Modifica la forma en la que se elimina el objeto.
    def __del__(self):
        print("Se ha eliminado el cd")



mi_cd = CD('pink', 'the wall', 24)

print(mi_cd)
print(len(mi_cd))

del mi_cd