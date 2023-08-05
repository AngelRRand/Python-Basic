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
    print(count)
    print(lis)

contar_primos(20)

