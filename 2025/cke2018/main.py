file = open("2025/cke2018/sygnaly.txt", 'r').read()
sygnaly = file.splitlines()

#4.1
i = 39
slowa = []
przeslanie = ""
while i < len(sygnaly):
    slowa.append(sygnaly[i])
    i += 40
for j in range(len(slowa)):
    przeslanie += slowa[j][9]
print(przeslanie)

#4.2
maksliterki = 0
zestawliterek = []
for i in range(len(sygnaly)):
    literki = []
    if len(set(sygnaly[i])) > maksliterki:
        maksliterki = len(set(sygnaly[i]))
        zestawliterek = sygnaly[i]
print(maksliterki,zestawliterek)

#4.3
for i in range(len(sygnaly)):
    check = True
    for a in range(len(sygnaly[i])):
        for b in range(a, len(sygnaly[i])):
            if abs(ord(sygnaly[i][a])-ord(sygnaly[i][b])) > 10:
                check = False
                break
    if check: print(sygnaly[i])
