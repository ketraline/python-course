tekst = "Litwo ojczyzno moja-Mickiewicz"
n = int(input("podaj rozmiar tabeli "))

tekst = tekst.upper()
while (len(tekst))%(n**2) != 0:
    tekst = tekst + "^"

if n == 1:
    print(tekst)
else:
    szyfr = ""
    k = 0 
    l = n**2
    for i in range(n**2):
        fragment = tekst[k:l]
        for j in range(n):
            kawalek = fragment[j::n]
            szyfr = szyfr + kawalek
        k += n**2
        l += n**2
    print(szyfr)

if n == 1:
    print(tekst)
else:
    kod = ""
    k = 0 
    l = n**2
    for i in range(n**2):
        fragment = szyfr[k:l]
        for j in range(n):
            kawalek = fragment[j::n]
            kod = kod + kawalek
        k += n**2
        l += n**2
    kod = kod.split("^")
    print(kod[0])