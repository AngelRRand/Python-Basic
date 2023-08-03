texto = "En la tranquila bruma de la mañana, una solitaria hoja de otoño caía, dibujando danzas en el viento. El susurro de la naturaleza, eterno y suave."

""" Primero """
lista_de_letras = []
lista_de_letras.append(input("Ingresa una letra: ").lower())
lista_de_letras.append(input("Ingresa una letra: ").lower())
lista_de_letras.append(input("Ingresa una letra: ").lower())
texto_min = texto.lower()

""" Segundo """
lista = texto.split()

""" Cuarto """
lista_invertida = lista[::-1]
texto_invertido = " ".join(lista_invertida)

""" Quinto """
aparecePython = "python" in texto
dic = {True: 'si', False: 'no'}


""" MENSAJES """

print("\n")
print(f"1 - La cantidad de veces que la letra \"{lista_de_letras[0]}\" en tu texto es: {texto_min.count(lista_de_letras[0])}")
print(f"1 - La cantidad de veces que la letra \"{lista_de_letras[1]}\" en tu texto es: {texto_min.count(lista_de_letras[1])}")
print(f"1 - La cantidad de veces que la letra \"{lista_de_letras[2]}\" en tu texto es: {texto_min.count(lista_de_letras[2])}")

print("\n")
print(f"2 - La cantidad de palabras en el texto es de: {len(lista)}")

print("\n")
print(f"3 - La primera letra en el texto es \"{texto[0]}\" y la ultima es \"{texto[-2]}\"")

print("\n")
print(f"4 - Tu texto invertido se ve asi: {texto_invertido}")

print("\n")
print(f"5 - En tu texto la palabra python {dic[aparecePython]} esta en el texto.")

