lista = ["meow","pies","meow"]
lista.remove("meow")
print(lista)

lista2 = ["banan", "banan","banan","banan","banan","banan","banan","banan"]
for x in lista2:
    print(x)

lista3 = ["1","7","6","8","2","3","13","15","24","37"]
lista3 = [eval(i) for i in lista3]
lista3.sort()
print(lista3)