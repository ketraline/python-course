### Liczby szczęśliwe (0-12)

Są to liczby wybrane zgodnie z algorytmem:

1. Pierwszą liczbą szczęśliwą jest liczba 1.
2. Wykreślamy wszystkie wartości parzyste, np.:

1
~~2~~
3
~~4~~
5
~~6~~
7
~~8~~
9
~~10~~
11
~~12~~
13
~~14~~
15
~~16~~
17
~~18~~
19
~~20~~
21
~~22~~
23
~~24~~
25
~~26~~
27
~~28~~
29
~~30~~
31
~~32~~
33
~~34~~
35
~~36~~
37
~~38~~
39
~~40~~
41
~~42~~
43
~~44~~
45
~~46~~
47
~~48~~
49
~~50~~
51
~~52~~
53
~~54~~
55
~~56~~

3. Druga liczba, która nie została wykreślona, to 3. Jest ona liczbą szczęśliwą.
4. Wykreślamy __co trzecią__ liczbę naturalną spośród pozostałych wszystkich liczb naturalnych dodatnich, zaczynając od liczby 1.
5. Trzecia liczba, która nie została wykreślona to 7. Jest ona liczbą częśliwą.
6. Wykreślamy __co siódmą__ liczbę.
7. Czwarta niewykreślona liczba to 9. Jest ona liczbą szczęśliwą.
8. Kolejną liczby szczęśliwą odnajdziemy wykreślając __co dziewiątą__ liczbę spośród wszystkich pozostałych liczb naturalnych, nastepnie __co trzynastą__ itd.

Te liczby, które "miały szczęście" i nie zostały skreślone, nazywamy _liczbami szczęśliwymi_. Kolejne początkowe liczby szczęśliwe to 1,3,7,9,13,15,21,25,31,33...

W pliku dane.txt zapisano liczby całkowite dodatnie po jednej w każdym wierszu. Każda liczba jest z zakresu od 0 do 10000. Napisz program (lub programy) dający 
odpowiedzi do poniższych zadań. Zapisz uzyskane odpowiedzi w pliku wyniki1.txt, poprzedzając każdą z nich numerem odpowiedniego zadania.

__Zadanie 1.1__ (0-6) Podaj, ile z podanych liczb jest liczbami szczęśliwymi.

__Zadanie 1.2__ (0-4) W pliku dane.txt znajdź najdłuższy ciąg następujących kolejno po sobie liczb szczęśliwych. Podaj długość ciągu oraz jego pierwszy wyraz.

__Zadanie 1.3__ (0-2) Niektóre z liczb szczęśliwych są również liczbami pierwszymi. Podaj, ile z podanych liczb to jednocześnie liczba szczęśliwa i liczba pierwsza.


### Liczby palindromiczne (0-7)

To takie liczby naturalne, które nie zmieniają się po zapisaniu ich cyfr w odwrotnej kolejności:

A. Pierwsze: 2,3,5,7,11,101,131,151...
B. Kwadratowe: 0,1,4,9,121,484,676,10201,12321...
C. Sześcienne: 0,1,8,343,1331,1030301,1367631...
D. Binarne: 0,1,11,101,111,1001,1111...

__Uwaga:__ Przyjmujemy, że liczby palindromiczne zapisujemy w najkrótszej możliwej postaci, tzn. bez ewentualnych zer wiodących.

__Zadanie 2.1__ (0-1) Sprawdź, które liczby sześciocyfrowe palindromiczne w systemie dwójkowym są jednocześnie liczbami palindromicznymi w systemie dziesiętnym.

__Zadanie 2.2__ (0-6) Napisz program, który znajdzie sumę wszystkich liczb mniejszych niż milion, które są palindromiczne jednocześnie w systemie dziesiętnym i dwójkowym.

Do oceny oddajesz:
    - plik wynik2_2.txt zawierający odpowiedź do zadania (jedną liczbę oznaczającą sumę liczb palindromicznych)
    - plik (pliki) z komputerową realizacją zadania (kodem programu).