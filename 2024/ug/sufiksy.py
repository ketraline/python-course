# Funckja czy_mniejszy daje TAK gdy sufiks s[k1:] < w porzadku alfabetycznym of s[k2:n]
def czy_mniejszy(n, s, k1, k2):
    i = k1
    j = k2
    while i < n and j < n:
        if s[i] == s[j]:
            i+=1
            j+=1
        else:
            if s[i] < s[j]:
                return "TAK"
            else:
                return "NIE"
    if j < n:
        return "TAK"
    else:
        return "NIE"

# 2.2
file = open("sufiks_2.txt", "r")
slowa = file.read()
slowa = slowa.replace(" ", "\n")
slowa = slowa.split("\n")
slowa.pop()

n = 10
s = "mascarpone"
k1 = int(slowa[2])
k2 = int(slowa[3])

print(czy_mniejszy(n, s, k1, k2))

# 2.3
alfslowo = sorted(s)
T = []
i = 0
while i < n:
    T.append(0)
    i+=1
i = 0
while i < n:
    suffix = s[i:]
    j = 0
    index = 0
    while j < n:
        if czy_mniejszy(n,s,j,i) == "TAK":
            index += 1
        j+=1
    print(suffix, index)
    T[index] = i+1
    i+=1
print(T)

# 2.4
file = open("slowa4.txt", "r")
slowa4 = file.read()
slowa4 = slowa4.split("\n")
a=0
suffixindex = 0
while a < len(slowa4)-1:
    slowa = slowa4[a].split(' ')
    slowo = [*slowa[1]]
    alfslowo = sorted(slowo)
    i = 0
    while i < int(slowa[0]):
        j = 0
        while j < int(slowa[0]):
            if alfslowo[i] == slowo[j]:
                suffixindex = "".join(slowo).rindex(alfslowo[i])
                break
            else:
                j+=1
        if suffixindex == "".join(slowo).rindex(alfslowo[i]):
            break
        i+=1
    print("".join(slowo[suffixindex:]))
    a+=1
