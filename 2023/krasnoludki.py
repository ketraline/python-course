a = "My jestesmy krasnoludki, hopsasa, hopsasa"
b = a[3:11]
print("1.1 "+"Zmienna b ma wartość = ", b)
c = a[-7:]
print("1.2 "+"Zmienna c ma wartość = ", c)
d = a[0:2]
print("1.3 "+"Zmienna d ma wartość = ", d.lower())
e = a[12:23]
print("1.3 "+"Zmienna e ma wartość = ", e.upper())
print("1.4 "+"Zmienna e ma wartość = ", e.lower())
print("1.5 "+"Zmienna d ma wartość = ", d.capitalize())
print("1.6 "+d+" "+b+" "+e+", "+c+", "+c)

I="Rwdogrbnrimlnvsspponbnf"
N="gClkjrvrtudrusjfdoveseh"

Wi = I[::3]
Wn = N[1::4]
print(f"2. {Wi}{Wn}")

print(f"3. W zmiennej a wystepuje {a.count('s')} liter s oraz {a.count('a')} liter a")

p = "Pxrxogxxrxamxoxwaxnixxexx xtxo xcxzexxscx ixnfxoxxrxxmxaxtxyxkxxixxx."
print(f"4. p.replace('x', '')")

liczba1 = input("podaj pierwsza liczbe ")
liczba2 = input("podaj druga liczbe ")
print(f"5. Suma = {int(liczba1) + int(liczba2)}, Roznica = {int(liczba1) - int(liczba2)}, Potega 3 stopnia {liczba1} = {int(liczba1)**3}, Potega 3 stopnia {liczba2} = {int(liczba2)**3}, Reszta z dzielenia przez 7 liczby {liczba1} = {int(liczba1)%7}, Reszta z dzielenia przez 7 liczby {liczba2} = {int(liczba2)%7}")

A = '\033[1;33;46m'
B = '\033[1;30;41m'
C = '\033[1;31;44m'
re = '\033[0m'
print(C + "Programowanie" + re + " " + A + "jest" + re + " " + B + "SUPER" + re)

rzymska1 = input("podaj 1 liczbe rzymska ")
if rzymska1 == "I":
    rzymska1 = 1
elif rzymska1 == "V":
    rzymska1 = 5
elif rzymska1 == "X":
    rzymska1 = 10
elif rzymska1 == "L":
    rzymska1 = 10
elif rzymska1 == "C":
    rzymska1 = 100
elif rzymska1 == "D":
    rzymska1 = 500
elif rzymska1 == "M":
    rzymska1 = 1000
else:
    print("to nie jest liczba rzymska")
rzymska2 = input("podaj 2 liczbe rzymska ")
if rzymska2 == "I":
    rzymska2 = 1
    print(rzymska1 + rzymska2)
elif rzymska2 == "V":
    rzymska2 = 5
    print(rzymska1 + rzymska2)
elif rzymska2 == "X":
    rzymska2 = 10
    print(rzymska1 + rzymska2)
elif rzymska2 == "L":
    rzymska2 = 10
    print(rzymska1 + rzymska2)
elif rzymska2 == "C":
    rzymska2 = 100
    print(rzymska1 + rzymska2)
elif rzymska2 == "D":
    rzymska2 = 500
    print(rzymska1 + rzymska2)
elif rzymska2 == "M":
    rzymska2 = 1000
    print(rzymska1 + rzymska2)
else:
    print("to nie jest liczba rzymska")
