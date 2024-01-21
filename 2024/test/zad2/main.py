plik = open("2024/test/zad2/liczby.txt", "r")
tekst = plik.read()
tekst = tekst.split('   ')
tekst.pop()
tekst = list(map(int, tekst))
print(tekst)
# 2a
print(max(tekst))
print(min(tekst))

# 2b
print("liczby ktore sie powtarzaja\n")
i=0
l = 1
repeat = tekst[i]
while i <1000:
    while l < 1000:
        if repeat == tekst[l]:
            print(repeat)
        else:
            l+=1
    i += 1

# 2c
print("liczby podzielne przez 13\n")
o = 0
while o < 1000:
    if tekst[o]%13 == 0:
        print(tekst[o])
    o += 1

# 2f