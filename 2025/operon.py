def wynik(n):
    if n == 1: return 2
    if n == 2: return -1
    if n == 3: return 1
    if n > 3: return wynik(n-1) + wynik(n-2) + wynik(n-3)

def wyniki(n):
    wyniki = [2, -1, 1]
    if n > 3:
        for i in range(3,n):
            wyniki.append(wyniki[i-1]+wyniki[i-2]+wyniki[i-3])
    return wyniki[n-1]

for i in range(1,11):
    print(i, wynik(i))
    print(i, wyniki(i))