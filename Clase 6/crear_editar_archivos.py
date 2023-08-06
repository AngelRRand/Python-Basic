""" Ejercicio 1 """
print("\n")
mi_archivo = open("./texto/editar.txt", "w")
mi_archivo.write("Mi nuevo texto")
mi_archivo.close()
mi_archivo = open("./texto/editar.txt", "r")
print(mi_archivo.read())
mi_archivo.close()

""" Ejercicio 2 """
print("\n")
mi_archivo = open("./texto/editar.txt", "a")
mi_archivo.write("\nNuevo inicio de sesion.")
mi_archivo.close()
mi_archivo = open("./texto/editar.txt", "r")
print(mi_archivo.read())
mi_archivo.close()

""" Ejercicio 3 """
print("\n")



registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

mi_archivo = open("./texto/registro.txt", "a")

for t in registro_ultima_sesion:
    mi_archivo.write(f"\n{t}")

mi_archivo.close()

mi_archivo = open("./texto/registro.txt", "r")
print(mi_archivo.read())
