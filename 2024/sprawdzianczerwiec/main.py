file = open("przyklad.txt", "r")
anagram = file.read()
anagram = anagram.split("\n")
anagram.pop()

#1.1
i = 0
rown = 0
prown = 0
while i < len(anagram):
    zera = 0
    jedynki = 0
    j=0
    liczba = anagram[i]
    liczba.split()
    while j < len(liczba):
        if liczba[j] == "0":
            zera+=1
        else:
            jedynki+=1
        j+=1
    if zera == jedynki:
        rown +=1
    elif abs(zera - jedynki) == 1:
        prown +=1
    i+=1

print(rown, prown)

#1.2
i = 0
anagramy8 = []
while i < len(anagram):
    if len(anagram[i]) == 8:
        anagramy8.append(anagram[i])
    i+=1

i = 0
najwanagramy = []
while i < len(anagramy8):
    zera = 0
    jedynki = 0
    j=0
    while j < 8:
        if anagramy8[i][j] == "0":
            zera+=1
        else:
            jedynki+=1
        j+=1
    if (jedynki >= zera) and zera >= 3:
        najwanagramy.append(anagramy8[i])
    i += 1
print(najwanagramy)

#1.3
i = 1
decy = 0
najwabs = 0
liczba1=0
while i < len(anagram):
    liczba = 0
    decy = int(anagram[i])
    while decy != 0:
        liczba += liczba + decy % 10
        decy = decy // 10
    if najwabs < abs(liczba1 - liczba):
        najwabs = abs(liczba1 - liczba)
    liczba1 = liczba
    i+=1
liczba = ""
while najwabs != 0:
    liczba += str(najwabs % 2)
    najwabs = najwabs // 2
i = len(str(liczba))-1
binliczba = ""
while i != 0:
    binliczba += liczba[i]
    i-=1
print(binliczba)

#1.3
i=0
brakzero =0
liczby9 = []
while i < len(anagram):
    liczba = 0
    decy = int(anagram[i])
    while decy != 0:
        liczba += liczba + decy % 10
        decy = decy // 10
    dziewiatkowy = int(anagram[i])
    while dziewiatkowy != 0:
        liczba += liczba + decy % 9
        dziewiatkowy = decy // 9
    liczby9.append(liczba)
    j = 0
    while j < len(str(liczba)):
        if str(liczba)[j] == 0:
            break
        else: j+=1
    if j == len(str(liczba)):
        brakzero +=1
    i +=1
print(brakzero)
#----------------------
#2
file = open("szachy_przyklad.txt", "r")
szachy = file.read()

#2.1
i = 1
a=0
puste = 0
wiersze = szachy.split("\n")
while i < len(wiersze):
    j = 0
    k = 0
    while k < 8:
        while j < 8:
            if wiersze[j][k] != ".":
                break
            else:
                j += 1
        if j == 8:
            puste+=1
        k += 1
    i+=1

print(puste)

#2.2
i = 0
rown = 0
czbierki = 0
bibierki = 0
minbierek = 0
j = 0
while i < len(wiersze):
    k = 0
    while j < i+8:
        while k < 8:
            if wiersze[j][k] != ".":
                if j < 4:
                    czbierki +=1
                else:
                    bibierki +=1
            k+=1
        j+=1
    if czbierki == bibierki:
        rown += 1
        if minbierek > (czbierki + bibierki):
            minbierek = czbierki + bibierki
    i+=8
    j+=8

print(rown, minbierek)
