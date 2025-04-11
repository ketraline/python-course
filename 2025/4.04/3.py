liczby = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60, 64, 72, 75, 80, 81, 90, 96, 100, 108, 120, 125, 128, 135, 144, 150, 160, 162, 180, 192, 200, 216, 225, 240, 243, 250, 256, 270, 288, 300, 320, 324, 360, 375, 384, 400, 405, 432, 450, 480, 486, 500, 512, 540, 576, 600, 625, 640, 648, 675, 720, 729, 750, 768, 800, 810, 864, 900, 960, 972, 1000, 125, 135, 150, 162, 180, 200, 216, 225, 243, 250, 270, 300, 324, 375, 400]


"""
Liczby dobre to takie, między którymi zachodzi relacja b % a == 0

W liście cyfr znajdź piątki takich liczb (a, b, c, d, e), między, którymi zachodzi relacja e % d == 0, d % c == 0, c % b == 0 i b % a == 0

Zapisz je w formacie listy [a, b, c, d, e]
"""
liczby.sort()
for a in liczby:
    if a*16 not in liczby:
        liczby.remove(a)
print(liczby)

piatki = [] 
for i in range(len(liczby)):
    for j in range(i+1, len(liczby)):
        for k in range(j+1,len(liczby)):
            for l in range(k+1, len(liczby)):
                for m in range(l+1, len(liczby)):
                    if (liczby[m]%liczby[l]==0) and (liczby[l]%liczby[k]==0) and (liczby[k]%liczby[j]==0) and (liczby[j]%liczby[i]==0):
                        piatki.append((liczby[i],liczby[j],liczby[k],liczby[l],liczby[m])) 
print(set(piatki))