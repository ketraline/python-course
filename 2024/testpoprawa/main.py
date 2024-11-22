#1
file = open("2024\\testpoprawa\dane.txt")
liczby = file.read()
file.close()
liczby = liczby.splitlines()
palindromiczne = []
#1.1
palindromcount = 0
osemka = 0
osemkowe = []
for i in range(len(liczby)):
    osemka = oct(int(liczby[i]))
    osemkowe.append(osemka[2:])
for i in range(len(osemkowe)):
    if osemkowe[i] == osemkowe[i][::-1]:
        palindromcount += 1
        if liczby[i] not in palindromiczne:
            palindromiczne.append(liczby[i])
file = open("wyniki1.txt", 'w')
file.write(f'1.1 Palindromy osemkowe: {palindromcount}\n')

#1.2
palindromcount = 0
czworkowe = []
for i in range(len(liczby)):
    czworkowa=""
    a = int(liczby[i])
    while a != 0:
        czworkowa = str(a%4) + czworkowa
        a = a//4
    czworkowe.append(czworkowa)
for i in range(len(czworkowe)):
    if czworkowe[i] == czworkowe[i][::-1]:
        palindromcount += 1
        if liczby[i] not in palindromiczne:
            palindromiczne.append(liczby[i])
file.write(f'1.1 Palindromy czworkowe: {palindromcount}\n')
file.close()

#1.3
for i in range(len(liczby)):
    if str(bin(int(liczby[i])))[2:] == (str(bin(int(liczby[i])))[2:])[::-1]:
        if liczby[i] not in palindromiczne:
            palindromiczne.append(liczby[i])
for i in range(len(liczby)):
    if str(hex(int(liczby[i])))[2:] == (str(hex(int(liczby[i])))[2:])[::-1]:
        if liczby[i] not in palindromiczne:
            palindromiczne.append(liczby[i])
print(palindromiczne)
#-------
#2
file = open("2024\\testpoprawa\liczby.txt")
liczby = file.read()
file.close()
liczby = liczby.splitlines()

#2.1
odwrotne = False
listaodwrotnych = []
for i in range(len(liczby)):
    if liczby[i] == liczby[i][::-1]:
        odwrotne = True
        listaodwrotnych.append(liczby[i])
file = open("wyniki2.txt", 'w')
file.write(f'2.1 Czy sa odwrotne liczby: {odwrotne}\nLista liczb: {listaodwrotnych}\n')

#2.2
suma = 0
count = 0
for i in range(len(liczby)):
    for j in range(len(liczby)):
        if liczby[i] == liczby[j][::-1]:
            if i != j:
                suma = int(liczby[i])+int(liczby[j])
                if str(suma)== str(suma)[::-1]:
                    count+=1
file.write(f'2.2 Liczba par {count}\n')

#3
file = open("wyniki3.txt", 'w')
file.write("3. 800 (10), 1100100000 (2)\n1111100010 (2), 2620 (7)\n1111202 (3), 44C (16)\n1301 (8), 10310 (5)\n19A (14), 408 (9)\n1177 (11), 22121 (5)")