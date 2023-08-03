texto = "En la tranquila bruma de la mañana, una solitaria hoja de otoño caía, dibujando danzas en el viento. El susurro de la naturaleza, eterno y suave."

letrasA = texto.count("a")
lista = texto.split()
aparecePython = "python" in texto


print(f"1 - La cantidad de veces que aparece la letra \"a\" es: {letrasA}")
print(f"2 - La cantidad de palabras en el texto es de: {len(lista)}")
print(f"3 - La primera letra en el texto es \"{texto[0]}\" y la ultima es \"{texto[-2]}\"")
print(f"4 - Tu texto invertido se ve asi: {texto[::-1]}")
print(f"5 - En tu texto la palabra python es {aparecePython}")

