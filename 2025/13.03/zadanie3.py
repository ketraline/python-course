liczby = open("2025/13.03/liczby.txt", 'r').read().splitlines()
for i in range(len(liczby)):
    liczby[i] = liczby[i].split(" ")
    liczby[i] = list(map(int,liczby[i]))
print(liczby)

#1.
minsuma = 10000000
maxsuma = 0
for i in range(len(liczby)):
    sumax = 0
    sumay = 0
    sumax = sum(liczby[i])
    if sumax > maxsuma: maxsuma = sumax
    if sumax < minsuma: minsuma = sumax
    j=0
    while j < len(liczby):
        sumay += liczby[j][i]
        j+=1
    if sumay < minsuma: minsuma = sumay
    if sumay > maxsuma: maxsuma = sumay
print(maxsuma, minsuma)

#2.
maxsuma = 0
minsuma = 10000000
for i in range(len(liczby)):
    for j in range(2,len(liczby)):
        sumax = 0
        sumax = liczby[i][j-2] + liczby[i][j-1] + liczby[i][j]
        if sumax > maxsuma: maxsuma = sumax
        if sumax < minsuma: minsuma = sumax
for i in range(len(liczby)):
    for j in range(2,len(liczby)):
        sumay = 0
        sumay = liczby[j-2][i] + liczby[j-1][i] + liczby[j][i]
        if sumay > maxsuma: maxsuma = sumay
        if sumax < minsuma: minsuma = sumax
print(maxsuma, minsuma)