from pathlib import Path, PureWindowsPath

""" PATHLIB """
ruta = "C:/Users/Horac/OneDrive/Escritorio/Orasio/Aprendiendo/11 Aprendiendo Python/Python Basic/Clase 6/texto/pathlib/texto.txt"


carpeta = Path(ruta)



#Lee el texto sin necesitadad de cerrarlo.
print(carpeta.read_text())

# Da el nombre el archivo.
print(carpeta.name)


# Da el tipo del archivo.
print(carpeta.suffix)


# Da el nombre el archivo sin la terminacion.
print(carpeta.stem)


# Revisar si existe o no el archivo
if not carpeta.exists:
    print("Este archivo no existe")
else:
    print("Este archivo si existe")



# Convertir la direccion en la de windows

nueva_ruta = "C:/Users/Horac/OneDrive/Escritorio/Orasio/Aprendiendo/11 Aprendiendo Python/Python Basic/Clase 6/texto\pathlib"

carpeta = PureWindowsPath(Path(nueva_ruta))

nuevo_archivo = carpeta / "otro_texto.txt" 

print(open(nuevo_archivo).read())


""" PATH """

# Devuelve el directorio principal
base = Path.home()
print(base)


# Crea una ruta apartir de strings
guia = Path("Hola", "Mundo", "Saludo.txt")
print(guia)

# Generar otra ruta de archivo desde el mismo PATH
guia2 = guia.with_name("Despedida.text")
print(guia2)

# Devuelve el archivo antecesor del path

parent = guia.parent
print(parent)

