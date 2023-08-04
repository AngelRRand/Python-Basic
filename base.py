""" Ejercicio 1 """
print("\n")

def cantidad_atributos(*args, **kwargs):
    print(len(args) + len(kwargs))

cantidad_atributos(1,2,3,4,x=10,y=10,z=10)

""" Ejercicio 2 """
print("\n")

def lista_atributos (**kwargs):
    return list(kwargs.values())

print(lista_atributos(a = 1, b = 1, c = 1))


""" Ejercicio 3 """
print("\n")



def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}: \n")
    for n,v in kwargs.items():
        print(f"{n}: {v} \n") 


describir_persona("María", color_ojos="azules", color_pelo="rubio")