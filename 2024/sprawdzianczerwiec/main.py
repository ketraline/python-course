file = open("2024\sprawdzianczerwiec\\przyklad.txt", "r")
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
file = open("wyniki1.txt","w")
file.write(f"1.1 Zrownowazone: {rown} Prawie zrownowazone: {prown}")

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
file.write(f"1.2 {najwanagramy}")

#1.3
i = 1
najwabs = 0
liczba1=0
while i < len(anagram):
    liczba = 0
    potega = 1
    binarna = int(anagram[i])
    while binarna != 0:
        resz = binarna % 10
        binarna = binarna // 10
        liczba += resz*potega
        potega = potega*2
    if najwabs < abs(liczba1 - liczba):
        najwabs = abs(liczba1 - liczba)
    liczba1 = liczba
    i+=1
liczba = ""
while najwabs != 0:
    liczba = liczba + str(najwabs % 2)
    najwabs = najwabs // 2
print(liczba[::-1])
file.write(f"1.3 {liczba[::-1]}")

#1.4
filedziewiec = open("liczby9.txt", "w")
i = 0
brakzero = 0
liczby9 = []
while i < len(anagram):
    liczba = 0
    potega = 1
    liczba9 = ""
    binarna = int(anagram[i])
    while binarna != 0:
        resz = binarna % 10
        binarna = binarna // 10
        liczba += resz*potega
        potega = potega*2
    while liczba != 0:
        resz = liczba % 9
        liczba = liczba // 9
        liczba9 = str(resz) + liczba9
    filedziewiec.write(f"{str(liczba9)}\n")
    j = 0
    while j < len(liczba9):
        if liczba9[j] == "0":
            break
        else: j+=1
    if j == len(liczba9):
        brakzero +=1
    i += 1
print(brakzero)
file.write(f"1.3 {brakzero}")

#----------------------
#2
file = open("2024\sprawdzianczerwiec\szachy_przyklad.txt", "r")
dane = []
for i in file:
    dane.append(i.strip())

i = 0
plansze = [[]]
while i < len(dane):
    row = dane[i]
    if row == '':
        plansze.append([])
    else:
        plansze[-1].append(row)
    i += 1

if plansze[-1] == []:
    plansze.pop()

#2.1

puste = []
p=0
while p < len(plansze):
    plansza=plansze[p]
    pustekolumny = 0
    i=0
    while i < len(plansza):
        pusta=True
        j=0
        while j < len(plansza):
            if plansza[j][i] != '.':
                pusta=False
                break
            j+=1
        if pusta == True:
            pustekolumny += 1
        i+=1
    if pustekolumny > 0:
        puste.append(pustekolumny)
    p+=1

file = open("wyniki1.txt","w")
file.write(f"2.1 {len(puste)} {max(puste)}")

#2.2

bierki = ['k', 'w', 's', 'h', 'g', 'p']
rownplansz = 0
minbierek = 1000

for plansza in plansze:
    bierkinaplanszy = []
    i = 0
    while i < len(plansza):
        j=0
        while j < len(plansza):
            if plansza[i][j] != '.':
                bierkinaplanszy.append(plansza[i][j])
            j += 1
        i += 1

    rownowaga = True
    for bierka in bierki:
        if bierkinaplanszy.count(bierka) != bierkinaplanszy.count(bierka.upper()):
            rownowaga=False
            break
    if rownowaga == True:
        rownplansz +=1
        if minbierek > len(bierkinaplanszy):
            minbierek = len(bierkinaplanszy)
file.write(f"2.2. {rownplansz} {minbierek}")


# 2.3

szachb = 0
szachcz = 0

for plansza in plansze:
    i=0
    while i < len(plansza):
        wiersz = ''.join(plansza[i])
        wiersz = wiersz.replace('.', '')
        characters = []
        j=0
        while j < len(plansza):
            characters.append(plansza[j][i])
            j+=1
        kolumna = ''.join(characters).replace('.', '')

        szachownica = [wiersz, kolumna]
        szach = [('k', 'W'), ('K', 'w')]

        for tekst in szachownica:
            for k, w in szach:
                if k in tekst and w in tekst:
                    kindex = tekst.index(k)
                    if kindex > 0 and tekst[kindex - 1] == w:
                        if w == "W": szachb += 1 
                        else: szachcz += 1
                    elif kindex < len(tekst) - 1 and tekst[kindex + 1] == w:
                        if w == "W": szachb += 1 
                        else: szachcz += 1
        i+=1

file.write(f"2.3. {szachb} {szachcz}")

