# 1

line = []
full = []
count = 0

with open("2023/szachy/szachy_przyklad.txt", "r") as tekst:
    for k in tekst:
        if count%9<8:
            line.append(k.strip())
        else:
            full.append(line.copy())
            line.clear
        count += 1

print(*full[0], sep = "\n")

for i in range(len(full)):
    for j in range(8):
        print(full[j][i], end = "    ")
    print()

print(zpl[3,3])
# 1
x = 0
y = 0
i = 0
col0=[]
while i < 150:
    while x < 8 and y < 8:
        col0 += full[i][x][y]
        if col0 != '.':
            col0.clear()
            x += 1
            y=0
        else:
            y += 1
    i += 0 