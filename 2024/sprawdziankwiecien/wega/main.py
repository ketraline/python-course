plik = open("2024/sprawdziankwiecien/wega/przyklad_WEGA.txt", "r")
signal = plik.read()

#4.1
slist = signal
slist = slist.split('\n')
slist.pop()
i = 39
word = ""
while i < 1000:
    word = word + str(slist[i][9])
    i += 40
print(word)
f = open("wynikwega.txt","a")
f.write(f"4.1: {word}")

#4.2
words = ""
maxword = ""
count = 0
i = 0
while i < 1000:
    letters = []
    j = 0
    wordb = slist[i]
    wordb.split()
    while j < len(wordb):
        if wordb[j] in letters:
            j+= 1
        else:
            letters.append(wordb[j])
            j += 1
    if len(letters) > count:
        count = len(letters)
        maxword = str(slist[i])
    i += 1
print(count, maxword)

f.write(f"\n4.2: {count} {maxword}")

#4.3
wordlist = []

for i in range(len(slist)):  
    for j in range(len(slist[i])):
        litera = 0
        for k in range(len(slist[i])):
            if abs(ord(slist[i][j]) - ord(slist[i][k])) > 11:
                litera+=1
    if litera == 0:
        wordlist.append(slist[i])
print(wordlist)
f.write(f"\n4.3: {wordlist}")
