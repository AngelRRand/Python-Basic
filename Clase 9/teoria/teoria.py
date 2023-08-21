# Saber en que directorio estamos parados 
import os
import shutil
print(os.getcwd(), "holis")



archivo = open("miTexto.txt", "w")
archivo.write("Texto de prueba")
archivo.close()



shutil.move("miTexto.txt", f"{os.getcwd()}/texto") 