x = int(input("podaj liczbe do spotegowania "))
p = int(input("podaj liczbe do ktorej chcesz podniesc potege "))
i = 0
wynik = 1

for i in range(p):
    wynik = wynik * x
    i+= 1
print(wynik, "wykonano ", i, " petle/i")