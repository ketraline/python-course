# Jeśli polecenie do zadania nie wskazuje inaczej, obowiązują następujące zastrzeżenia:
# Twój algorytm może używać wyłącznie zmiennych przechowujących liczby całkowite oraz może operować wyłącznie na liczbach całkowitych.
# W zapisie możesz wykorzystać tylko operacje arytmetyczne: dodawanie, odejmowanie, mnożenie, dzielenie, dzielenie całkowite,
# resztę z dzielenia oraz porównywanie liczb, instrukcje sterujące, przypisania do zmiennych lub samodzielnie napisane funkcje,
# wykorzystujące wyżej wymienione operacje. Zabronione jest używanie funkcji wbudowanych oraz operatorów innych niż wymienione.

"""
1. Poniżej znajdziesz program, którego działanie definiują dwie funkcje.

Na podstawie analizy odpowiedz na pytanie - do czego służy ten program i/lub jego funkcje?

Czy jest to implementacja jakiegoś algorytmu? Jeśli tak, to jakiego?

Zapisz listę kroków, pomagających w uzyskaniu odpowiedzi na powyższe pytanie

Na podstawie analizy zmień nazwy funkcji, ich argumentów oraz pomocniczych zmiennych na opisowe (to znaczy takie, których nazwy wskazywać będą na
przeznaczenie / sposób działania / oczekiwaną odpowiedź z funkcji - podobnie jak np funkcja len(x), gdzie x: str
zwraca liczbę stanowiącą długość ciągu znaków x lub arr_length = len(x) definiuje zmienną, w której przechowywana jest ta długość).

Jeżeli którakolwiek z funkcji lub jej wywołań zawiera niepotrzebne (tj. nic nie wnoszące) lub błędne operacje, popraw ją.
"""

def Euklides(a,b):
    if b == 0:
        return a
    else:
        return z(b, a%b)


def test(i,j):
    if i != j:
        return f"Failed"
    else:
        return f"Passed"

test(Euklides("a","b"), "c")
