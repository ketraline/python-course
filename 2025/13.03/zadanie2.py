dane = open("2025/13.03/dane.txt", 'r').read().splitlines()
print(dane)

for i in range(len(dane)):
    for j in range(i,len(dane)):
        if len(dane[j]) < len(dane[i]):
            x = dane[j]
            dane[j] = dane[i]
            dane[i] = x
        if len(dane[j]) == len(dane[i]):
            if dane[j] < dane[i]:
                x = dane[j]
                dane[j] = dane[i]
                dane[i] = x 
haslo = ""
for i in range(len(dane)):
    haslo += dane[i][0] + dane[i][-1]
print(haslo)