"""
2. Napisz program (lub programy), który znajdzie takie słowa z pliku words.txt,
których kolejne litery występują po sobie w alfabecie i zwróć je w formie słownika o kształcie:

{
    "słowo": długość słowa # tu: 5
}

Na przykład:
- "begin" to słowo składające się z liter następujących po sobie w alfabecie (a, b, c, d, e)
- "chinos" to słowo składające się z liter następujących po sobie w alfabecie (f, g, h, i, j)
- "python" to NIE jest słowo składające się z liter następujących po sobie w alfabecie

Dodatkowo:
- Funkcja powinna ignorować wielkość liter (traktować "AbCdE" tak samo jak "abcde").
- Funkcja powinna działać poprawnie dla słów o różnej długości (minimum 2 znaki).
- Funkcja powinna ignorować wszystkie nie-litery (cyfry, znaki specjalne) i sprawdzać tylko litery.
- Jeśli słowo zawiera tylko jedną literę, nie powinno być uznawane za spełniające warunek.

Napisz również funkcję testującą test_identify_sequential_words(), która weryfikuje poprawność działania Twojej funkcji, uwzględniając różne przypadki testowe.

Przykłady:
1. identify_sequential_words(["abcde", "python", "fghij", "hello"]) powinno zwrócić {"abcde": 5, "fghij": 5}
2. identify_sequential_words(["xyz", "computer", "ABCD", "123"]) powinno zwrócić {"xyz": 3, "ABCD": 4}
"""

words = open("2025/4.04/words.txt", "r").read().splitlines()
print(words)
slownik = {}

for i in range(len(words)):
    word = []
    check = True
    for j in range(len(words[i])):
        word.append(words[i][j])
    for j in range(1,len(word)):
        if word[j-1] > word[j]: check = False
    if check: slownik[words[i]] = len(words[i])

print(slownik)