from math import sqrt
#1
coords = [[-3,4],[3,7],[1,-4],[6,-6],[11,0],[4,-1],[sqrt(3)+1,0.5]]
minlength = 9999999999999999999999999
for i in range(0,len(coords)):
    for j in range(i+1,len(coords)):
        x = coords[i][0]-coords[j][0]
        y = coords[i][1]-coords[j][1]
        length = sqrt(pow(x,2)+pow(y,2))
        if length < minlength:
            minlength = length
            mincoords = [coords[i], coords[j]]
print(f'#1 najmniejsza dlugosc {minlength} dla {mincoords}\n')

#2
maraton = [[34,1], [78,4], [48,2], [19,3]]
def sort(m):
    for i in range(len(m)):
        for j in range(i,len(m)):
            if m[i][0] > m[j][0]:
                m[i], m[j] = m[j], m[i]
    return m
sort(maraton)
j = 1
for i in range(len(maraton)):
    while j < len(maraton)+1:
        maraton[i].append(j)
        j+=1
        break
print("#2 dane: minuty, uczestnik, miejsce")
print(maraton, "\n")

#3
przedzialy = [[1, 5], [3, 7], [8, 10]]
sort(przedzialy)
j=0
print(przedzialy)
for i in range(len(przedzialy)-1):
    for j in range(len(przedzialy)-1):
        if i != j:
            if przedzialy[i][0] <= przedzialy[j][0] <= przedzialy[i][1]:
                przedzialy[i][1] = przedzialy[j][1]
                del(przedzialy[j])

print(przedzialy)

#4
lista = [0,0,0,2,4,5,6,6,7,7,7,8,9,4,3,5,6]
count = 1
liczba = []
maxcount=0
def sort2(m):
    for i in range(len(m)):
        for j in range(i,len(m)):
            if m[i] > m[j]:
                m[i], m[j] = m[j], m[i]
    return m
sort2(lista)
print(lista)
for i in range(1,len(lista)):
    if lista[i-1] == lista[i]:
        count +=1
        if lista[i] not in liczba:
            liczba.append(lista[i])
    else:
        print(i,count,liczba,lista[i])
        if maxcount == count:
            if liczba[0]<liczba[1]:
                liczba.pop()
            else:
                liczba.pop(1)
        if maxcount < count:
            maxcount = count
            liczba.clear()
            liczba.append(lista[i])
