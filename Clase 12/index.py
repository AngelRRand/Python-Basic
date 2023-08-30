from tkinter import *



# Iniciar tkinter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry("1020x630")

# Evitar maximizar
aplicacion.resizable(0, 0)

# titulo de la ventana
aplicacion.title("Restaurante - Sistema de facturacion")

# Color de fondo
aplicacion.config(bg="burlywood")

# Panel superior
panel_Superior = Frame(aplicacion)
panel_Superior.pack(side=TOP)

# Etiquieta titulo
etiqueta_titulo = Label(panel_Superior, text="Sistema de facturacion", fg="white", font=("Dosis", 25), bg="black", width=55)
etiqueta_titulo.grid(row=0, column=0)


# Panel izquierdo
panel_izquierdo = Frame(aplicacion)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(aplicacion, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Comidas", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
panel_comidas.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
panel_postres.pack(side=LEFT)

# Panel izquierdo
panel_derecha = Frame(aplicacion)
panel_derecha.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha, bg="burlywood")
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecha, bg="burlywood")
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecha, bg="burlywood")
panel_botones.pack()






# lista de productos
lista_comidas = ["pollo", "cordero", "salmon", "merluza", "kebab", "hamburgueza", "carne"]

lista_bebidas = ["agua", "soda", "jugo", "vino1", "vino2", "cerveza1", "cerveza2"]

lista_postres = ["helado", "fruta", "brownies", "flan", "mousse", "pastel1", "banana"]





# Generar items comida
variables_comida = []

contador = 0
for comida in lista_comidas:
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=("Dosis", 19, "bold"), onvalue=1, offvalue=0, variable=variables_comida[contador])
    comida.grid(row=contador, column=0, sticky=W)
    contador += 1


# Generar items bebidas
variables_bebidas = []
contador = 0
for bebidas in lista_bebidas:
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebidas = Checkbutton(panel_bebidas, text=bebidas.title(), font=("Dosis", 19, "bold"), onvalue=1, offvalue=0, variable=variables_bebidas[contador])
    bebidas.grid(row=contador, column=0, sticky=W)
    contador += 1

# Generar items postres
variables_postres = []
contador = 0
for postres in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres, text=postres.title(), font=("Dosis", 19, "bold"), onvalue=1, offvalue=0, variable=variables_postres[contador])
    postres.grid(row=contador, column=0, sticky=W)
    contador += 1













# evitar que la pantalla se cierre
aplicacion.mainloop()