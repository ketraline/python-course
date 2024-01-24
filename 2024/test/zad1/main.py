plik = open("2024/test/zad1/tablica.txt", "r")
tekst = plik.read()
tablica = tekst

# 1a
tekst = tekst.splitlines()
x = int(input("Podaj pozycje od 0 do 9 "))
linijka = tekst[0][x] + tekst[1][x] + tekst[2][x] + tekst[3][x] + tekst[4][x] + tekst[5][x] + tekst[6][x] + tekst[7][x] + tekst[8][x] + tekst[9][x]

print(linijka, "\n")

# 1b
print(tablica)

# 1c
i = 0
while i<10:
    print(tekst[0][i] + tekst[1][i] + tekst[2][i] + tekst[3][i] + tekst[4][i] + tekst[5][i] + tekst[6][i] + tekst[7][i] + tekst[8][i] + tekst[9][i])
    i += 1
