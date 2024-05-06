plik = open("2024/piksele/dane.txt", "r")
tekst = plik.read()
rows = tekst.split('\n')
j=0
while j < len(rows):
    rows[j]=rows[j].split(' ')
    j+=1

a = 19
while a < 29:
    row = []
    b = 19
    while b < 29:
        row.append(rows[a][b])
        b+=1
    print(row)
    a+=1