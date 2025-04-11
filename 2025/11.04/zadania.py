from random import randint

# 1A. W pliku entry_arr.txt znajduje się lista liczb z zakresu <1,10000>
# spośród, których część spełnia zależność e % d == 0, d % c == 0, 
# c % b == 0, b % a == 0
# Na podstawie przeprowadzonej analizy napisz funkcję, która znajdzie te
# piątki i zwróci je w postaci macierzy (tablicy tablic), a także zwróci
# ilość tych piątek.

array = open("2025/11.04/entry_arr.txt", 'r').read().splitlines()
array = list(map(int,array))
print(array)
def piatkichecker(lista):
    lista.sort()
    piatki = []
    for a in range(len(lista)):
        for b in range(a+1, len(lista)):
            if lista[b]%lista[a] == 0:
                for c in range(b+1, len(lista)):
                    if lista[c]%lista[b] == 0:
                        for d in range(c+1, len(lista)):
                            if lista[d]%lista[c] == 0:
                                for e in range(d+1, len(lista)):
                                    if lista[e]%lista[d] == 0:
                                        piatki.append([lista[a],lista[b],lista[c],lista[d],lista[e]])
    return piatki
print(piatkichecker(array))

# 1B. Napisz funkcję, która przygotuje listę stu unikalnych liczb z zakresu
# <1, 10000>, spośród których część spełni zależność e % d == 0, d % c == 0, 
# c % b == 0, b % a == 0
# Zapisz otrzymaną listę do pliku my_numbers.txt
# Wykorzystując funkcję przygotowaną w zadaniu 1A sprawdź poprawność listy.

def generator():
    liczby = []
    while not piatkichecker(liczby):
        x = 0
        while x < 100:
            random = randint(1,10000)
            while random in liczby:
                random = randint(1,10000)
            liczby.append(random)
            x+=1
    return liczby, piatkichecker(liczby)

print(generator())    