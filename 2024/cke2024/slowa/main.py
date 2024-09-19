'''
Zadanie 3. Słowa
W pliku slowa.txt danych jest 1000 słów (napisów) złożonych z małych liter alfabetu
angielskiego. Słowa mają długość mieszczącą się w przedziale od 1 do 200 znaków.
Napisz program(-my), dający(-e) odpowiedzi do poniższych zadań. Uzyskane odpowiedzi
zapisz w pliku wyniki3.txt, a każdą z nich poprzedź numerem odpowiedniego zadania.
Do Twojej dyspozycji jest plik slowa_przyklad.txt, który zawiera 10 słów w podanym
formacie. Odpowiedzi dla tego pliku są podane w treści zadań. Pamiętaj, że Twój program
musi ostatecznie działać dla pliku slowa.txt, zawierającego 1000 słów.
'''
import re
file = open('2024/cke2024/slowa/slowa_przyklad.txt')
words = file.read()
words = words.splitlines()

#1 Podaj, w ilu spośród podanych słów znajduje się trójliterowy fragment "k?t", gdzie ? oznacza dowolną pojedynczą literę (taki fragment występuje na przykład w słowach "alamakota", albo "brokat", ale nie – w słowie "krata".)
count = 0
for i in range(len(words)):
    if re.findall(r"k.t", words[i]) != []:
        count+=1
print("1.1:", count)

'''
Alfabet angielski zawiera 26 liter. Kodowanie ROT13 zamienia każdą literę na literę, która
jest na pozycji o 13 miejsc dalej w alfabecie (a→n, b→o itd.), przy czym po przekroczeniu „z”
liczymy z powrotem od „a” (czyli m→z, ale n→a, o→b, i tak dalej).
Słowo aren ma ciekawą własność – po zakodowaniu za pomocą ROT13 staje się słowem
nera, czyli tym samym słowem czytanym od tyłu.
Podaj, ile w pliku slowa.txt jest słów, które mają tę własność. Wypisz ich liczbę oraz
najdłuższe z nich.
'''
count = 0
maxword = ""
rot13 = str.maketrans("abcdefghijklmnopqrstuvwxyz","nopqrstuvwxyzabcdefghijklm")
for i in range(len(words)):
    word = words[i]
    rot13word = str.translate(word, rot13)
    if word == ''.join(list(rot13word)[::-1]8):
        count += 1
        if len(maxword) < len(word):
            maxword = word

print("1.2", count, maxword)

'''
Zadanie 3.3. (0–3)
Znajdź i wypisz z pliku slowa.txt wszystkie takie słowa, w których ta sama litera
występuje na co najmniej połowie pozycji (przykładowo: w słowie "owocowo" litera „o” ma 4
wystąpienia na ogólną liczbę 7 liter w słowie i spełnia podany warunek, za to w słowie
"ambaras" litera „a” ma tylko 3 wystąpienia na 7 liter, więc nie spełnia podanego warunku).
'''
print("1.3")
halfwords = []
letter = 0
for i in range(len(words)):
    word = list(words[i])
    for j in range(len(word)):
        letter = word.count(word[j])
        if letter >= (len(word)/2):
            print(''.join(word))
            break
