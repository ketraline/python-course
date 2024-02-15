#3.1
N = 20
SITO = []
for i in range(0,N+1):
    SITO.append(i)
SITO[1] = False

print(SITO)
for i in range(2,N):
    SITO[i] = True

for i in range(2,N):
    if SITO[i] == True:
        j = i * i
        while j <= N:
            SITO[j] = False
            j = i + j
print(SITO)

# 3.2 Dla każdej liczby x z pliku liczby.txt sprawdź, czy liczba x – 1 jest liczbą pierwszą. 
# Podaj, ile liczb z pliku liczby.txt po pomniejszeniu o 1 daje liczbę pierwszą.

plik = open("2024/cke2023/liczby/liczby_przyklad.txt", "r")
numbers = plik.read()
numbers = numbers.splitlines()
print(numbers)
for i in range (0,100):
    numbers[i] -= 1