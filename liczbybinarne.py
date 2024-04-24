f = open('liczby.txt')
liczby = f.read()
liczby = liczby.split('\n')
liczby = list(map(int, liczby))
i = 0
index = 0
biggest = 0
while i < len(liczby):
    r = 0
    x = liczby[i]
    while x != 0:
        r = r + x % 10
        x = x // 10
    if r > biggest:
        biggest = r
        index = i+1
    i += 1
print(biggest, liczby[index])