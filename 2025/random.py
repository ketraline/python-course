# Twój algorytm może używać wyłącznie zmiennych przechowujących liczby całkowite oraz może operować wyłącznie na liczbach całkowitych. 
# W zapisie możesz wykorzystać tylko operacje arytmetyczne: dodawanie, odejmowanie, mnożenie, dzielenie, dzielenie całkowite, 
# resztę z dzielenia oraz porównywanie liczb, instrukcje sterujące, przypisania do zmiennych lub samodzielnie napisane funkcje, 
# wykorzystujące wyżej wymienione operacje. Zabronione jest używanie funkcji wbudowanych oraz operatorów innych niż wymienione.

# 1. Napisz funkcję generującą listę x losowych unikalnych liczb z zakresu 1 do 10001.
import random
def Random(x):
    lista = []
    while len(lista) < x:
        i = random.randint(1,10001)
        if i not in lista: 
            lista.append(i)
    return lista

a = Random(10)
print(a)

# 2. Napisz funkcję, która przyjmie jako argument listę i zwróci:
# - "błąd! ❌" jeśli lista zawierać będzie duplikaty,
# - "wszystko ok ✅" jeśli będzie się składać z samych unikalnych argumentów.
def checkDuplicates(n):
    if len(set(n)) < len(n):
        return "błąd! ❌"
    else:
        return "wszystko ok ✅"
print(checkDuplicates(a))

# 3. Napisz funkcję, która przyjmie jako argument listę liczb całkowitych i zwróci nową listę z tymi samymi elementami, 
# ale posortowanymi rosnąco. Możesz użyć dowolnego algorytmu sortowania, który da się zaimplementować 
# przy użyciu dozwolonych operacji. Przetestuj funkcję na liście wygenerowanej przez generate_random_unique_numbers.

def listSorter(n):
    i = 1
    while i < len(n):
        if n[i-1] > n[i]:
            temp = n[i]
            n[i] = n[i-1]
            n[i-1] = temp
            i = 0
        i += 1
    return n
print(listSorter(a))

# 4. Napisz funkcję, która przyjmie jako argument listę liczb całkowitych i zwróci medianę tej listy. 
# Jeśli lista ma parzystą liczbę elementów, zwróć średnią arytmetyczną dwóch środkowych elementów. 
# Funkcja powinna działać poprawnie nawet jeśli lista nie jest posortowana (możesz użyć funkcji sortującej z poprzedniego zadania). 
# Przetestuj funkcję na liście wygenerowanej przez generate_random_unique_numbers.

def listMedian(n):
    n = listSorter(n)
    if len(n) % 2 == 0:
        return (n[int(len(n)/2)] + n[int(len(n)/2) - 1])/2
    else:
        return n(len(n)//2)
print(listMedian(a))

# 5. Napisz funkcję, która implementuje wyszukiwanie binarne w posortowanej liście liczb całkowitych. 
# Funkcja powinna przyjmować dwa argumenty: posortowaną listę liczb całkowitych oraz liczbę do znalezienia. 
# Powinna zwracać indeks, pod którym znajduje się szukana liczba, lub -1, jeśli liczba nie występuje w liście. 
# Przetestuj funkcję na posortowanej liście wygenerowanej przez generate_random_unique_numbers, 
# wyszukując zarówno elementy obecne w liście, jak i nieobecne.
a.append(10000)
def binarySearch(n, o):
    n = listSorter(n)
    if o not in n: return -1
    if o == n[len(n)//2]:
        return n[len(n)//2]
    else:
        while len(n) > 1:
            split1 = n[0:len(n)//2]
            split2 = n[len(n)//2: len(n)]
            print(split1,split2)
            if o > split2[0]:
                n = split2
                add += len(split1)
            elif o == split2[0]: return i
            else: n = split1
print(binarySearch(a, 10000))