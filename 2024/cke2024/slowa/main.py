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
print(count)

#2
count = 0
maxword = ""
rot13 = str.maketrans("abcdefghijklmnopqrstuvwxyz","nopqrstuvwxyzabcdefghijklm")
for i in range(len(words)):
    word = words[i]
    rot13word = str.translate(word, rot13)
    if word == ''.join(list(rot13word)[::-1]):
        count += 1
        if len(maxword) < len(word):
            maxword = word

print(count, maxword)

#3 
halfwords = []
letter = 0
for i in range(len(words)):
    word = list(words[i])
    for j in range(len(word)):
        letter = word.count(word[j])
        if letter >= (len(word)/2):
            print(''.join(word))
            break
