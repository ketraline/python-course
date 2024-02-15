plik = open("2023/cke2023/mecz/mecz_przyklad.txt", "r")
tekst = plik.read()

#1.1
a = tekst.split("AB")
b = tekst.split("BA")
print(len(a)+len(b)-2)

#1.2
winsA = 0
winsB = 0
for i in range(len(tekst)):
    if tekst[i] == "A":
        winsA += 1
    else:
        winsB += 1

    if winsA >= 1000 and winsA >= winsB+3 or winsB >= 1000 and winsB >= winsA+3:
        print("pierwszy set w ", winsA, ":", winsB)
        break

#1.3
passaA = 0
passaB = 0
countA = 0
countB = 0
for i in range(len(tekst)):
    if tekst[i+countA] == "A":
        countA+=1
    else:
        countA = 0
    if tekst[i+countB] == "B":
        countB+=1
    else:
        countB = 0
    if countA >= 10:
        passaA += 1
    if countB >= 10:
        passaB += 1

print(passaA, passaB)
        



    