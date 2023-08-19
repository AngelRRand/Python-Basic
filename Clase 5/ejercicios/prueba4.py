def contar_primos(num):
    count = 0
    lis = [2]
    for n in range(num):
        if n < 2:
            continue
        for i in range(2, int(n**0.5) + 1):

            if n % i == 0:
                break
        else:
            count += 1
            lis.append(n)

contar_primos(20)

def contar_primos(num):
    primos = [2]
    iteracion = 3
    if num <2:
        return 0
    while iteracion <=0:
        for n in range(3,iteracion,2):
            if iteracion %n ==0:
                iteracion +=2
                break
        else:
            primos.append(iteracion)
            iteracion +=2
    return len(primos)