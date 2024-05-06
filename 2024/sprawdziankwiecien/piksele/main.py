plik = open("2024/sprawdziankwiecien/piksele/dane.txt", "r")
tekst = plik.read()

#6.1
minimax = tekst.replace('\n', ' ')
minimax = minimax.split(' ')
minimax.pop()
minimax = list(map(int, minimax))
print("najjasniejszy:", max(minimax))
print("najciemniejszy:", min(minimax), "\n")
f = open("wynikpixele.txt","a")
f.write(f"6.1: najciemniejszy {min(minimax)} najjasniejszy {max(minimax)}")

#6.2
rows = tekst.split('\n')
delete = 0
i = 0
while i < 200:
    row = rows[i]
    row = row.split(' ')
    row = list(map(int, row))
    j=0
    while j < (len(row)/2):
        if row[j] == row[len(row)-1-j]:
            j += 1
        else:
            j=0
            delete += 1
            break
    i+= 1
print(delete)
f.write(f"\n6.2: {delete}")

#6.3
rows = tekst.split('\n')
q=0
while q < 200:
    rows[q]=rows[q].split(' ')
    rows[q] = list(map(int, rows[q]))
    rows[q].insert(0, rows[q][0])
    rows[q].insert(320, rows[q][318])
    q+=1
rows.insert(0, rows[0])
rows.insert(200, rows[200])
i=1
contrast = 0
while i < 200:
    j=1
    while j < 320:
        if abs(rows[i][j]-rows[i+1][j]) > 128:
            contrast +=1
        elif abs(rows[i][j]-rows[i-1][j]) > 128:
            contrast +=1 
        elif abs(rows[i][j]-rows[i][j+1]) > 128:
            contrast +=1 
        elif abs(rows[i][j]-rows[i][j-1]) > 128:
            contrast +=1 
        j+=1
    i+=1
print(contrast)
f.write(f"\n6.3: {contrast}")

#6.4
rows = tekst.split('\n')
j=0
while j < len(rows):
    rows[j]=rows[j].split(' ')
    j+=1
line = 1
longest = 0
i = 0
while i < 320:
    j=0
    while j < 200:
        if j > 0:
            if rows[j-1][i] == rows[j][i]:
                line += 1
            else:
                line = 1
        if line > longest:
            longest = line
        j+=1
    i+=1
print(longest)
f.write(f"\n6.4: {longest}")
