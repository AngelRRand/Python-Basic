vendedor = input('¿Cual es tu nombre?')
ventas = int(input('¿Cuanto has vendido?'))

comision = round(ventas * 13 /100, 2)

print(f"Hola {vendedor} tu dinero sera de {comision}")