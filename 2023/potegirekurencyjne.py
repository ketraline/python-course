a = 2 
x = 100
t = 0
def potega(z,y):
    global t
    if y == 0:
        wynik = 1
        return wynik
    if y%2 ==0:
        p = potega(z,y//2)
        wynik = p*p
        t +=1
    else:
        p = potega(z,(y-1)//2)
        wynik = z*p*p
        t+=1
    return wynik
print(potega(a,x), t)