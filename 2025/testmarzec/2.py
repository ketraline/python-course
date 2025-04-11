"""
2. (Razem: 8 pkt) Napisz program (lub programy) do konwersji liczb z dowolnego systemu pozycyjnego między 2 a 19 na system dziesiętny. 
W przypadku systemów pozycyjnych 17,18,19 przyjmij, że kolejne cyfry reprezentowane są przez litery alfabetu analogicznie do systemu
szesnastkowego.
Twoja funkcja powinna przyjąć liczbę do konwersji jako ciąg dużych znaków (np. "ABC") oraz podstawę systemu jako liczbę całkowitą.
W przypadku, gdy podana liczba do konwersji zawierać będzie znaki reprezentujące cyfry nie istniejące w zadeklarowanym systemie
pozycyjnym, Twój program powinien zwrócić błąd, np.

convert("ABC", 5) # powinno zwrócić błąd, ponieważ w piątkowym systemie pozycyjnym "A" nie reprezentuje żadnej liczby, gdyż posługuje się on 
wyłącznie liczbami 0,1,2,3,4.

Napisz funkcję testującą rezultat działania Twojego konwertera, która zwróci "błąd ❌" gdy oczekiwany wynik będzie niezgodny z otrzymanym
lub "test zaliczony ✅" w przeciwnym wypadku.
Funkcja testowa powinna sprawdzać przypadki skrajne i poprawnie obsługiwać błędne dane wejściowe

Np.:

test(convert("A", 16), 10) -> "test zaliczony ✅" 
"""

def convert(a,S):
    if S == 10: return(a)
    if type(a) != str: raise Exception(f"Argument A must be a string")
    W = 0
    for i in a:
        if i in "ABCDEFGHIJ":
            if S < 11: raise Exception(f"Letter {i} cannot be converted in system {S}")
            for j in range(len("ABCDEFGHIJ")):
                if i == "ABCDEFGHIJ"[j]: break
            W = W * S + int(translate[1][j])
        else:
            W = W * S + int(i)
    return W
translate = [["A","B","C","D","E","F","G","H","I","J"],[10,11,12,13,14,15,16,17,18,19]]

def test(x,y,z):
    if convert(x,y) == z: return "test zaliczony ✅"
    else: return "błąd ❌"

print(test("45256",8,777))
print(test("ABCDEF",16,11259375))
print(test("A8FI3",19,1670383))