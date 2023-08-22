import time
import timeit


def prueba_for(num):
    res = []
    for n in range(1, num + 1):
        res.append(n)
    return res


def prueba_while(num):
    res = []
    count = 1
    while count <= num:
        res.append(count)
        count += 1
    return res




inicio = time.time()
prueba_for(10)
final = time.time()
print(final - inicio)



inicio = time.time()
prueba_while(10)
final = time.time()
print(final - inicio)




""" CUANDO LOS PROCESOS SON MAS PEQUEÑOS Y MAS PRECISOS """


declaration = """
prueba_for2(10000)
"""

mi_setup = """
def prueba_for2(num):
    res = []
    for n in range(1, num + 1):
        res.append(n)
    return res
"""

duracion = timeit.timeit(declaration, mi_setup, number=100)
print(duracion)



declaration2 = """
prueba_while(10000)
"""


mi_setup2 = """
def prueba_while(num):
    res = []
    count = 1
    while count <= num: 
        res.append(count)
        count += 1
    return res
"""

duracion2 = timeit.timeit(declaration2, mi_setup2,number = 100)
print(duracion2)
