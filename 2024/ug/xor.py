f = open('liczby.txt')
liczby = f.read()
liczby = liczby.split('\n')
i = 0
j = 0
r=0
xor = 0
while i < len(liczby):
    liczba = liczby[i]
    liczba.split()
    while j < len(liczba):
        xor = xor + (int(liczba[j])+(int(liczba[j])//2))%2
        j += 1
    print(xor)
    i += 1