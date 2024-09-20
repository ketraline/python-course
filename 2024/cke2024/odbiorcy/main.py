file = open("odbiorcy_przyklad.txt")
odbiorcy = file.read()
odbiorcy = odbiorcy.splitlines()
odbiorcy = list(map(int, odbiorcy))
print(odbiorcy)
'''
4.2 - Dla danych zapisanych w pliku odbiorcy.txt podaj liczbę komputerów, które nie są
odbiorcami żadnych pakietów.
'''
count = 0
for x in range(len(odbiorcy)):
    if x+1 not in odbiorcy:
        count += 1
print(count)

'''
4.3 - W kolejnych rundach może się zdarzyć, że pakiet wróci do komputera, z którego został
początkowo wysłany (komputera o numerze takim, jaki ma ten pakiet).
Wyznacz najmniejszy numer rundy, w której którykolwiek pakiet powróci do komputera,
z którego startował (o tym samym numerze co numer tego pakietu).
Podaj najmniejszy numer takiego pakietu dla wyznaczonego numeru rundy.
'''
rundy = odbiorcy
for x in range(len(odbiorcy)):
    index = []
    for y in range(len(odbiorcy)):
        if odbiorcy[y] == x:
            index.append(y)
    for y in range(len(index)):
        rundy[index[y]] = odbiorcy[index[y]]
print(odbiorcy)
print(rundy)
