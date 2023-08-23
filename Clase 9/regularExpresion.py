import re
""" Ejercicio 1 """
print("\n")
def verificar_email(email):
    patron = r"\w+@\w+\.com.\w{2}"
    verificar = re.search(patron, email)
    if verificar:
        print("Todo OK")
    else:
        print("Todo mal")




verificar_email("Hola@ho.com.ar")

""" Ejercicio 2 """
print("\n")
def verificar_saludo(frase):
    patron = r"^Saludos"
    verificar = re.search(patron, frase)
    if verificar:
        print("Todo OK")
    else:
        print("Todo mal")


verificar_saludo("Buenas gente")
verificar_saludo("Saludos lindossss")

""" Ejercicio 3 """
print("\n")


def verificar_cp(cp):
    patron = r"^\w{2}\d{4}$"
    verificar = re.search(patron, cp)
    print(verificar)
    if verificar:
        print("Todo OK")
    else:
        print("Todo mal")

