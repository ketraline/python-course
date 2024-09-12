n = int(input())
szachownica = ""
liczba = "1"

for i in range(0, n*n):
    if liczba == "0":
        liczba = "1"
    else: 
        liczba = "0"
    szachownica = szachownica + liczba
for i in range(0, len(szachownica), n):
    print(szachownica[i:i+n])
