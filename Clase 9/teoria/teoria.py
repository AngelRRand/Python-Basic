# Saber en que directorio estamos parados 
import os
import shutil
import send2trash

ruta = os.getcwd()

archivo = open("miTexto.txt", "w")
archivo.write("Texto de prueba")
archivo.close()



shutil.move("miTexto.txt", f"{ruta}/texto") 

# Mueve el archivo a la papelera
send2trash.send2trash(f"{ruta}\\texto\\miTexto.txt")


for carpeta, subcarpeta, archivo in os.walk(f"{ruta}\\carpeta_padre"):
    print(f"En la carpeta: {carpeta}")
    print(f"La subcarpeta es: ")
    for sub in subcarpeta:
        print(f"\t{sub}")
        print(f"Los archivos son: ")
    for a in archivo:
        print(f"\t{a}")
    print("\n")


