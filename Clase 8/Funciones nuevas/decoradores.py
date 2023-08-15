def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otra_funcion

@decorar_saludo
def mayus(texto):
    print(texto.upper())


def minus(texto):
    print(texto.lower())

""" Ambas formas funcionan para decorar una funcion """

mayus("Horacio")

mayuscula_decorada = decorar_saludo(mayus)

mayuscula_decorada("Horaciooooo6")