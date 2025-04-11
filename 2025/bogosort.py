import random

lista = ["8","2","4","3"]

while lista != sorted(lista):
    lista2 = []
    i = len(lista)
    while i != 0:
        x = random.randint(0,len(lista)-1)
        lista2.append(lista[x])
        del lista[x]
        i -= 1
    lista = lista2
    print(lista)