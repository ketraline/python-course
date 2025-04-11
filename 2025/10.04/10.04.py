"""
ZADANIE 1 – DZIELNIKI W KOLEJNOŚCI

Masz tablicę (listę) 1000 różnych liczb całkowitych z zakresu od 1 do 100000.
Twoim zadaniem jest znaleźć wszystkie trójki liczb (a, b, c) z tej listy, które spełniają:

    a < b < c
    b dzieli się przez a (czyli b % a == 0)
    c dzieli się przez b (czyli c % b == 0)

Na przykład, jeśli lista zawiera liczby: [2, 4, 8], to pasuje trójka (2, 4, 8).

Spróbuj najpierw podejść "na piechotę" – sprawdzając wszystkie możliwe trójki.
Zastanów się, jak można to przyspieszyć.
"""
liczby = open("2025/10.04/liczby.txt", 'r').read().splitlines()
liczby = list(map(int,liczby))
liczby.sort()

trojki = []
for i in range(len(liczby)):
    for j in range(i+1, len(liczby)):
        if liczby[j]%liczby[i] == 0:
            for k in range(j+1,len(liczby)):
                if liczby[k]%liczby[j] == 0:
                    trojki.append((liczby[i],liczby[j],liczby[k]))
print(trojki)

"""
ZADANIE 2 – SUMA JAKO ELEMENT

Masz dwie listy A i B – każda zawiera 1000 liczb z przedziału od 1 do 1 000 000.

Zadanie: znajdź wszystkie pary (a, b), gdzie:
    a pochodzi z listy A,
    b pochodzi z listy B,
    a + b też znajduje się w liście A.

Przykład:
A = [3, 5, 8, 12]
B = [2, 3, 4]
Para (5, 3) pasuje, bo 5 + 3 = 8, a 8 jest w liście A.

Pomyśl, czy można jakoś szybciej sprawdzać, czy coś jest w liście A?
"""
A = open("2025/10.04/listaA.txt", 'r').read().splitlines()
A = list(map(int,A))
B = open("2025/10.04/listaB.txt", 'r').read().splitlines()
B = list(map(int,B))

pary = []
for i in A:
    for j in B:
        if i+j in A:
            pary.append((i,j))
print(pary)

"""
ZADANIE 3 – TRÓJKĄT Z LICZB

Masz listę 1000 różnych liczb naturalnych.

Twoje zadanie: znajdź wszystkie trójki (a, b, c), które mogą być bokami trójkąta.
Czyli muszą spełniać tzw. nierówność trójkąta:

    a + b > c
    a + c > b
    b + c > a

Przykład:
(3, 4, 5) to dobry trójkąt – warunki są spełnione.
(1, 2, 3) – nie pasuje (bo 1 + 2 nie jest większe niż 3).

Czy da się ograniczyć liczbę porównań, żeby nie sprawdzać wszystkiego?
"""
trojkat = []
for i in range(len(liczby)):
    for j in range(len(liczby)):
        for k in range(len(liczby)):
            if i+j > k and j+k>i and i+k > j:
                trojkat.append((liczby[i],liczby[j],liczby[k]))
print(trojkat)
"""
ZADANIE 4 – SUMY CYFR

Masz listę 1000 liczb całkowitych z przedziału od 1 do 100000.

Znajdź wszystkie trójki liczb (a, b, c) z tej listy, które spełniają warunek:

    b = suma cyfr liczby a
    c = suma cyfr liczby b

Przykład:
Jeśli lista zawiera: [123, 6, 6], to pasuje trójka:
    a = 123 (1 + 2 + 3 = 6)
    b = 6
    c = 6 (bo suma cyfr 6 to znowu 6)

Czy da się wcześniej policzyć wszystkie sumy cyfr i zapisać wyniki?
"""
