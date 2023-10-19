#Znaleźć najdłuzszy ciąg liter A i B; jaka maja długość; gdzie sie zaczynają i kończa w słowie źródłowym

import re
plik = open("2023/r2/tekst.txt", "r")
tekst = plik.read()
div = re.split('AB|BA', tekst)

a = [x for x in div if x.startswith("A")]
b = [x for x in div if x.startswith("B")]

finda = max(a)
print("najdluzszy string a:", finda, "dlugosc", len(finda), "poczatek", tekst.find(finda), "koniec", tekst.find(finda)+len(finda))
findb = max(b)
print("najdluzszy string a:", findb, "dlugosc", len(findb), "poczatek", tekst.find(findb), "koniec", tekst.find(findb)+len(findb))

