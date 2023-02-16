x = "jakas zmienna"
print(x[0]) #czyta 1 znak zmiennej
print(x[2:]) #czyta wszystko po 2 zmiennej
print(x[:5]) #czyta wszystko do 5 zmiennej
print(x[::2]) #robi krok co 2 znaki

name = "karolina"
lastname = "leszczynska"

nsn = name + lastname
print(nsn)
print(name * 3, lastname, end="!!!!!!!")
print(name * 3, lastname)

#type() sprawdza typ zmiennej

li = input("podaj liczbe")
print(int(li)+ 56)

jb = 7
print(str(jb).zfill(3))