# Jeśli polecenie do zadania nie wskazuje inaczej, obowiązują następujące zastrzeżenia:
# Twój algorytm może używać wyłącznie zmiennych przechowujących liczby całkowite oraz może operować wyłącznie na liczbach całkowitych. 
# W zapisie możesz wykorzystać tylko operacje arytmetyczne: dodawanie, odejmowanie, mnożenie, dzielenie, dzielenie całkowite, 
# resztę z dzielenia oraz porównywanie liczb, instrukcje sterujące, przypisania do zmiennych lub samodzielnie napisane funkcje, 
# wykorzystujące wyżej wymienione operacje. Zabronione jest używanie funkcji wbudowanych oraz operatorów innych niż wymienione.

"""
Napisz program (lub programy), który w tablicy liczb znajdzie dwie liczby dające największą i dwie liczby dające najmniejszą średnią.
- Gdy jako argument podana zostanie pusta tablica lub lista jednoargumentowa, Twój program powinine zwrócić odpowiedni błąd.
- Program nie powinien brać do obliczeń dwukrotnie tego samego argumentu.

Np. tablica = [1,2,3,4]
Największą średnią dają liczby 3 i 4 (nie 4 i 4)
Najmniejszą średnią dają liczby 1 i 2 (nie 1 i 1)
"""
tablica = [1,2,3,4,5,6,7]

def minSrednia(x):
    mini = 10000000000.0
    wspolrzedne = [0,0]
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j:
                srednia = (x[i] + x[j])/2
                if srednia < mini:
                    mini = srednia
                    wspolrzedne = [x[i],x[j]]
    return mini, wspolrzedne

def maxSrednia(x):
    maxi = 0.0
    wspolrzedne = [0,0]
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j:
                srednia = (x[i] + x[j])/2
                if srednia > maxi:
                    maxi = srednia
                    wspolrzedne = [x[i],x[j]]
    return maxi, wspolrzedne
print(minSrednia(tablica), maxSrednia(tablica))


"""
Swoimi słowami opisz zasadę działania algorytmu wyszukiwania binarnergo.
Na przykładzie zapisz krok po kroku, jak przy pomocy tego algorytmu w tablicy [1,2,3,4,5] odnaleziona
zostałaby pozycja liczby 1.
Jaka jest jego przewaga tego algorytmu nad wyszukiwaniem liniowym?
"""
