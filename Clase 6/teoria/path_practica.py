from pathlib import Path, PureWindowsPath


ruta = "C:/Users/Horac/OneDrive/Escritorio/Orasio/Aprendiendo/11 Aprendiendo Python/Python Basic/Clase 6/texto"

base = PureWindowsPath(Path(ruta))

guia = Path(base, "America")

""" Glob """
# Con glob ve todo en la carpeta.
# Con el simbolo asterisco revisa la carpeta en la que se encuentra
# Con el doble revisa todas las carpetas dentro de su ubicacion.
 
for txt in Path(guia).glob("**/*.txt"):
    print(txt)

