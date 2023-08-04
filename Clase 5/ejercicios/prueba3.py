def muchos_ceros(*arg):
    for i, n in enumerate(arg):
        if n == 0 and arg[i] == arg[i + 1]:
            return True
    return False


print(muchos_ceros(6,0,0,5,1,0,3,0,1))