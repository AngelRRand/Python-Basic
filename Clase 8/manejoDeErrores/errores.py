""" Ejercicio 1 """
print("\n")
def suma(num1,num2):
        try:
            print(num1+num2)
        except:
            print("Error inesperado")
        else:
            print("Todo bien")
                
suma(1, 2)
suma(1, "hori")




""" Ejercicio 2 """
print("\n")


def cociente(num1,num2):
        
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
    else:
        print("Todo bien")    

cociente(10, 50)
cociente("a", 20)
cociente(4, 0)




""" Ejercicio 3 """
print("\n")



def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")

abrir_archivo("hori.txt") 
abrir_archivo("lorito.txt") 

