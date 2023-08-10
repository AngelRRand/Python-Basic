""" PROYECTO """
from random import randint

""" CODIGO """
print("\n")


print('Buenos dias usuario tiene 8 intentos para saber el numero en el que estoy pensado... ¡Te dare una pista! es un numero entre el 1 y el 100. Tranquilo con cada intento te dire si estas cerca. ')

print("\n")

numero_secreto = randint(1, 100)
intentos_usuarios = 8
carita = ":D"

while intentos_usuarios > 0:

    numero_usuario = int(input('Dime un numero entre el 1 y el 100. '))
    

    intentos_usuarios -= 1

    match intentos_usuarios:
        case 5:
            carita = ":)"
        case 4:
            carita = ":o"     
        case 3:
            carita = ":c"
        case 2:
            carita = ":("
        case 1:
            carita = "x_x"

    if (numero_usuario > 100) or (numero_usuario < 1):
        print("Debes ingresar un numero valido entre el 100 y el 0.")
        print(f"Te quedan {intentos_usuarios} intentos {carita}")
        print("\n")
    elif numero_usuario < numero_secreto:
        print("Tu numero es menor al numero secreto.")
        print(f"Te quedan {intentos_usuarios} intentos {carita}")
        print("\n")
    elif numero_usuario > numero_secreto:
        print("Tu numero es mayor al numero secreto.")
        print(f"Te quedan {intentos_usuarios} intentos {carita}")
        print("\n")
    else:
        print("Has ganado")
        print(f"Te ha tomado {8 - intentos_usuarios} intentos {carita}")
        print("\n")
        break
else:
    print(f"Lamentablemente has perdido... el numero secreto era {numero_secreto}")
    
