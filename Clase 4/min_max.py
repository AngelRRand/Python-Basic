""" Ejercicio 1 """
print("\n")

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo = max(lista_numeros)
print(valor_maximo)

""" Ejercicio 2 """

valor_minimo = int(min(lista_numeros))
rango = valor_maximo - valor_minimo
print(rango)




""" Ejercicio 3 """
print("\n")


diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}


edad_minima = min(diccionario_edades.values())
print(edad_minima)

ultimo_nombre = max(diccionario_edades)
print(ultimo_nombre)
