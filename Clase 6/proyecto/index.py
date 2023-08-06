from os import system
from pathlib import Path
import shutil

system("cls")

ruta = "/Users/Horac/OneDrive/Escritorio/Orasio/Aprendiendo/11 Aprendiendo Python/Python Basic/Clase 6/proyecto/Recetas"
nombre_usuario = input("Dime tu nombre: ")

texto_opciones = """
Elige una de las siguiente opciones: """

list_optiones_menu = {
    1: "Leer receta",
    2: "Crear receta",
    3: "Crear categoria",
    4: "Eliminar receta",
    5: "Eliminar categoria",
    6: "Finalizar programa"
}
    
system("cls")

def iniciar():
    opcion = 1
    last_option = len(list_optiones_menu)

    while opcion != last_option:

        print(f"Hola {nombre_usuario} tienes un total de {cantidad_recetas()} recetas")

        categoria = ""
        categorias = nombres_categoria()

        opcion = validar_opcion(list_optiones_menu)

        match opcion:
            case 1:
                """ LEER RECETA """
                system("cls")

                """ Categoria """
                print("Elije una opcion")
                opcion = validar_opcion(categorias)
                categoria = categorias[opcion]

                """ Receta """
                recetas =  nombres_recetas(categorias[opcion])
                system("cls")
                print("Elije una opcion")
                opcion = validar_opcion(recetas)
                
                ruta_receta = Path(ruta, categoria, recetas[opcion])

                leer(ruta_receta)

            case 2:
                """ CREAR RECETA """
                system("cls")

                """ Categoria """
                print("Elije una opcion")
                opcion = validar_opcion(categorias)
                categoria = categorias[opcion]

                crear_receta(categoria)

            case 3:
                """ CREAR RECETA """
                system("cls")

                crear_categoria()
            case 4:
                """ CREAR CATEGORIA """
                system("cls")

                """ Categoria """
                print("Elije una opcion")
                opcion = validar_opcion(categorias)
                categoria = categorias[opcion]

                """ Receta """
                recetas =  nombres_recetas(categorias[opcion])
                system("cls")
                print("Elije una opcion")
                opcion = validar_opcion(recetas)
                
                ruta_receta = Path(ruta, categoria, recetas[opcion])

                eliminar_receta(ruta_receta)
            case 5:
                """ CREAR CATEGORIA """
                system("cls")

                """ Categoria """
                print("Elije una opcion")
                opcion = validar_opcion(categorias)
                categoria = categorias[opcion]

                ruta_categoria = Path(ruta, categoria)
                
                eliminar_categoria(ruta_categoria)


    else:
        system("cls")
        print(f"Ejecucion terminada")
        return  
    

def nombres_categoria():
    dic = {}
    for i, carpeta_categoria in enumerate(Path(ruta).glob("*")):
        dic[i + 1] = carpeta_categoria.name
    
    return dic

def nombres_recetas(categoria):
    dic = {}
    for i, archivo_receta in enumerate(Path(ruta, categoria).glob("*.txt")):
        dic[i + 1] = archivo_receta.name
    return dic

def leer(ruta):
    system("cls")
    print(
        f"""
            ______________________________
          
            Tu receta dice: 
            {ruta.read_text()} 
            ______________________________
        """)
    

def crear_receta(categoria):
    system("cls")
    print(f"Estas creando una receta del tipo {categoria}")
    nueva_receta = input("Dime el nombre de tu nueva receta: ")
    nueva_ruta = Path(ruta, categoria, nueva_receta + ".txt")
    texto_receta = input("Escribe sobre tu receta: ")
    receta = open(nueva_ruta, "a")
    receta.write(texto_receta)
    receta.close()
    print(
        f"""
            ______________________________
          
            Receta creada exitosamente
            ______________________________
        """)

def crear_categoria():
    print(f"Estas creando una categoria")
    nueva_categoria = input("Dime que nombre ponerle: ")
    nueva_ruta = Path(ruta, nueva_categoria)
    nueva_ruta.mkdir(parents=True, exist_ok=True)
    print(
        f"""
            ______________________________
          
            Categoria creada exitosamente
            ______________________________
        """)

def eliminar_receta(ruta):
    system("cls")
    ruta.unlink()
    print(
        f"""
            ______________________________
          
            Receta eliminada exitosamente
            ______________________________
        """)

def eliminar_categoria(ruta):
    system("cls")
    shutil.rmtree(ruta)
    print(
        f"""
            ______________________________
          
            Categoria eliminada exitosamente
            ______________________________
        """)
    






""" FUNCIONES GLOBALES """

def validar_opcion(lista_opciones):

    options(lista_opciones)

    new_opcion = input(texto_opciones)
    
    while new_opcion.isdigit() == False or int(new_opcion) > len(lista_opciones):
        mensaje_error(lista_opciones)
        new_opcion = input(texto_opciones)
    else:
        option = int(new_opcion)
        return option
    
def options(options):
    for key, option in options.items():
        print(f"\n{key} - {option}")

def mensaje_error(lista_opciones):
    system("cls")
    print("Error... \n")
    print("Debes ingresar una opcion valida.")     
    options(lista_opciones) 
        
def cantidad_recetas():
    cantidad = 0
    for txt in Path(ruta).glob("**/*.txt"):
        cantidad += 1
    return cantidad


    



iniciar()