"""
1. (Razem: 8pkt) Poniżej znajdziesz program, którego działanie definiują dwie funkcje.

a) Na podstawie analizy odpowiedz na pytanie - do czego służy ten program? (1 pkt)

b) Czy jest to implementacja jakiegoś algorytmu? Jeśli tak, to jakiego? (1 pkt)

c) Zapisz listę kroków, pomagających w uzyskaniu odpowiedzi na powyższe pytanie (3 pkt)

d) Na podstawie analizy zmień nazwy funkcji, ich argumentów oraz pomocniczych zmiennych na opisowe (to znaczy takie, których nazwy wskazywać będą na
przeznaczenie / sposób działania / oczekiwaną odpowiedź z funkcji - podobnie jak np funkcja len(x), gdzie x: str 
zwraca liczbę stanowiącą długość ciągu znaków x lub arr_length = len(x) definiuje zmienną, w której przechowywana jest ta długość). (3 pkt)

Jeżeli którakolwiek z funkcji zawiera niepotrzebne (tj. nic nie wnoszące) operacje, popraw ją.
"""
'''
a) Funkcja sluzy do sortowania podanej listy integerow rosnaco
b) Merge sort
c) 1. Funkcja najpierw rodziela podana liste na 2 czesci: lewa i prawa dopoki nie zostanie w niej 1 element
      Powstaje takie drzewko, np.
      [5,7,8,9]       ^
    [5,9]   [7,8]     |
[9]   [5]   [8]   [7] |
   2. Funkcja porownuje lewa i prawa strone na samym dole drzewka i daje najmniejszy element na poczatku listy posortowanej
   3. Funkcja dodaje reszte elementow z drugiej strony do listy posortowanej
   4. Potem funckja porownuje do siebie posortowane listy z obu stron drzewka, dopoki cala lista nie bedzie spowrotem zlaczona w jedno

'''
def compareLeftAndRight(left: list, right: list) -> list:
    sortedList = []
    
    while left and right:
        if left <= right:
            sortedList.append(left.pop(0))
        else:
            sortedList.append(right.pop(0))
    sortedList.extend(left)
    sortedList.extend(right)
    return sortedList


def mergeSort(a: list) -> list:
    if len(a) <= 1:
        return a
    left = mergeSort(a[:(len(a) // 2)])
    right = mergeSort(a[(len(a) // 2):])
    return compareLeftAndRight(left, right)

print(mergeSort([2,5,6,3,4,5]))