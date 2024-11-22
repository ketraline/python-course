file = open("2024/liczby/dane.txt")
liczby = file.read()
liczby = liczby.splitlines()

decy = 0
bina = 0
octa = 0
hexa = 0
for i in range(len(liczby)):
    if liczby[i] == liczby[i][::-1]:
        decy +=1
    binarna = ""
    a = int(liczby[i])
    while a != 0:
        binarna = str(a%2) + binarna
        a = a//2
    if binarna == binarna[::-1]:
        bina += 1
    osemkowa = ""
    a = int(liczby[i])
    while a != 0:
        osemkowa = str(a%8) + osemkowa
        a = a//8
    if osemkowa == osemkowa[::-1]:
        octa += 1
    hexadecy = ""
    a = int(liczby[i])
    hexadecimal = str.maketrans("10","A")
    while a != 0:
        hexadecy = str(a%16) + hexadecy
        a = a//16
    if hexadecy == hexadecy[::-1]:
        hexa += 1
print(bina,octa,decy,hexa)

decy = 0
bina = 0
octa = 0
hexa = 0
for i in range(len(liczby)):
    if liczby[i] == liczby[i][::-1]:
        decy +=1
    if bin(int(liczby[i]))[2:] == (bin(int(liczby[i]))[2:])[::-1]:
        bina +=1
    if oct(int(liczby[i]))[2:] == (oct(int(liczby[i]))[2:])[::-1]:
        octa +=1
    if hex(int(liczby[i]))[2:] == (hex(int(liczby[i]))[2:])[::-1]:
        hexa +=1
print(bina,octa,decy,hexa)