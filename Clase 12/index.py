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
etiqueta_titulo = Label(
    panel_Superior,
    text="Sistema de facturacion",
    fg="white",
    font=("Dosis", 25),
    bg="black",
    width=55,
)
etiqueta_titulo.grid(row=0, column=0)


# Panel izquierdo
panel_izquierdo = Frame(aplicacion)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(
    panel_izquierdo,
    text="Comidas",
    font=("Dosis", 19, "bold"),
    bd=1,
    relief=FLAT,
    fg="azure4",
)
panel_comidas.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(
    panel_izquierdo,
    text="Bebidas",
    font=("Dosis", 19, "bold"),
    bd=1,
    relief=FLAT,
    fg="azure4",
)
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(
    panel_izquierdo,
    text="Postres",
    font=("Dosis", 19, "bold"),
    bd=1,
    relief=FLAT,
    fg="azure4",
)
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
lista_comidas = [
    "pollo",
    "cordero",
    "salmon",
    "merluza",
    "kebab",
    "hamburgueza",
    "carne",
]

lista_bebidas = ["agua", "soda", "jugo", "vino1", "vino2", "cerveza1", "cerveza2"]

lista_postres = ["helado", "fruta", "brownies", "flan", "mousse", "pastel1", "banana"]


# Generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # crea los checksbuttons
    variables_comida.append("")
    variables_comida[contador] = IntVar()
    comida = Checkbutton(
        panel_comidas,
        text=comida.title(),
        font=("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variables_comida[contador],
    )
    comida.grid(row=contador, column=0, sticky=W)

    # crear los cuadros de entrada
    cuadros_comida.append("")
    texto_comida.append("")
    texto_comida[contador] = StringVar()
    texto_comida[contador].set("0")
    cuadros_comida[contador] = Entry(
        panel_comidas,
        font=("Dosis", 19, "bold"),
        bd=1,
        width=6,
        state=DISABLED,
        textvariable=texto_comida[contador],
    )

    cuadros_comida[contador].grid(row=contador, column=1)

    contador += 1


# Generar items bebidas
variables_bebidas = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebidas in lista_bebidas:
    variables_bebidas.append("")
    variables_bebidas[contador] = IntVar()
    bebidas = Checkbutton(
        panel_bebidas,
        text=bebidas.title(),
        font=("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variables_bebidas[contador],
    )
    bebidas.grid(row=contador, column=0, sticky=W)

    # crear los cuadros de entrada
    cuadros_bebida.append("")
    texto_bebida.append("")
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set("0")
    cuadros_bebida[contador] = Entry(
        panel_bebidas,
        font=("Dosis", 19, "bold"),
        bd=1,
        width=6,
        state=DISABLED,
        textvariable=texto_bebida[contador],
    )

    cuadros_bebida[contador].grid(row=contador, column=1)

    contador += 1


# Generar items postres
variables_postres = []
cuadros_postre = []
texto_postre = []
contador = 0
for postres in lista_postres:
    variables_postres.append("")
    variables_postres[contador] = IntVar()
    postres = Checkbutton(
        panel_postres,
        text=postres.title(),
        font=("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variables_postres[contador],
    )
    postres.grid(row=contador, column=0, sticky=W)

    # crear los cuadros de entrada
    cuadros_postre.append("")
    texto_postre.append("")
    texto_postre[contador] = StringVar()
    texto_postre[contador].set("0")
    cuadros_postre[contador] = Entry(
        panel_postres,
        font=("Dosis", 19, "bold"),
        bd=1,
        width=6,
        state=DISABLED,
        textvariable=texto_postre[contador],
    )

    cuadros_postre[contador].grid(row=contador, column=1)

    contador += 1

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiquetas de osto y campos de entrada

etiqueta_costo_comida = Label(
    panel_costos, text="Costo comida", font=("Dosis", 15, "bold")
)
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(
    panel_costos,
    font=("Dosis", 15, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_costo_comida,
)
texto_costo_comida.grid(row=0, column=1, padx=41)


etiqueta_costo_bebida = Label(
    panel_costos, text="Costo bebida", font=("Dosis", 15, "bold")
)
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(
    panel_costos,
    font=("Dosis", 15, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_costo_bebida,
)
texto_costo_bebida.grid(row=1, column=1, padx=41)


etiqueta_costo_postre = Label(
    panel_costos, text="Costo postre", font=("Dosis", 15, "bold")
)
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(
    panel_costos,
    font=("Dosis", 15, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_costo_postre,
)
texto_costo_postre.grid(row=2, column=1, padx=41)



etiqueta_subtotal = Label(
    panel_costos, text="Subtotal", font=("Dosis", 15, "bold")
)
etiqueta_subtotal.grid(row=0, column=2)

texto_costo_subtotal = Entry(
    panel_costos,
    font=("Dosis", 15, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_subtotal,
)
texto_costo_subtotal.grid(row=0, column=3, padx=41)


etiqueta_impuesto = Label(
    panel_costos, text="Impuestos", font=("Dosis", 15, "bold")
)
etiqueta_impuesto.grid(row=1, column=2)

texto_costo_impuesto = Entry(
    panel_costos,
    font=("Dosis", 15, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_impuesto,
)
texto_costo_impuesto.grid(row=1, column=3, padx=41)



etiqueta_total = Label(
    panel_costos, text="Total", font=("Dosis", 15, "bold")
)
etiqueta_total.grid(row=2, column=2)

texto_costo_total = Entry(
    panel_costos,
    font=("Dosis", 15, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_total,
)
texto_costo_total.grid(row=2, column=3, padx=41)

# evitar que la pantalla se cierre
aplicacion.mainloop()
