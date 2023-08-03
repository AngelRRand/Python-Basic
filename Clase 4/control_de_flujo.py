""" Ejercicio 1 """

num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 == num2:
    print(f"{num1} y {num2} son iguales")
elif num1 > num2:
    print(f"{num1} es mayor que {num2}")
else :
    print(f"{num2} es mayor que {num1}")


""" Ejercicio 2 """


edad = 16
tiene_licencia = False


if edad >= 18:
    if tiene_licencia == True:
        print("Puedes conducir")
    else:
        print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")




""" Ejercicio 3 """



habla_ingles = True
sabe_python = False


if (habla_ingles == True) and (sabe_python == True):
    print("Cumples con los requisitos para postularte")
else:
    if habla_ingles == True:
        print("Para postularte, necesitas saber programar en Python")
    elif sabe_python == True:
        print("Para postularte, necesitas tener conocimientos de inglés")
    else:
        print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")


