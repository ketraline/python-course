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
    j=0
    row = rows[i]
    row = row.split(' ')
    row = list(map(int, row))
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