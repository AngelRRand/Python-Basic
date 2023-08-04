def devolver_distintos(*arg):
    res = sum(arg)
    num_max = max(arg)
    num_min = min(arg)

    if res > 15:
        print(num_max)
    elif res < 10:
        print(num_min)
    else:
        print(res - num_max - num_min)

        




devolver_distintos(10,2,2)