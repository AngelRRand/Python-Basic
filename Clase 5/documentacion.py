""" Ejercicio 1 """
print("\n")

text = ",:_#,,,,,,:::____##Python_ _Total,,,,,,::#"

lis = text.split()
for i, n in enumerate(lis):
    lis[i] = lis[i].lstrip(",:%_#")
    lis[i] = lis[i][::-1].lstrip(",:%_#")
    lis[i] = lis[i][::-1]
new_text = " ".join(lis)
print(new_text)

""" Ejercicio 2 """
print("\n")


frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 

frutas.insert(3, "naranja")

print(frutas)



""" Ejercicio 3 """
print("\n")


marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

print(marcas_smartphones.isdisjoint(marcas_tv))