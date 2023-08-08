def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except: 
            print("Ese numero no es valido")
        else:
            print(f"Has puesto el numero {numero}")
            break
    
    print("Gracias")


pedir_numero()