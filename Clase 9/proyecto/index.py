import os
import re
import datetime
import time
import math
from collections import deque
from pathlib import Path
from ticket import mensaje 


ruta = f"{os.getcwd()}\\Mi_Gran_Directorio"

def recorrer_carpetas():
    patron = r"N\w{3}\-\d{5}"
    hoy = datetime.date.today()
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        lista = deque()
        count = 0
        tiempo = 0
        inicio = time.time()
        for a in archivo:
            contenido = Path(ruta, carpeta, a).read_text()
            verificar = re.search(patron, contenido)
            if verificar:
                count += 1
                lista.append((a, verificar.group()))
            else:
                continue
        if count > 0:
            final = time.time()
            tiempo = math.ceil(final - inicio)
            mensaje(hoy, lista, count, tiempo)
        else:
            continue
            


                
recorrer_carpetas()

