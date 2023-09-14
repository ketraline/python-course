a = 'Nad rzeczka, opodal krzaczka miszkala Kaczka Dziwaczka.'

b=a[4:11]
print(f'1.1 zmienna b ma wartosc {b}')

c=a[-10:]
print(f'1.2 zmienna c ma wartosc {c}')

d=a[38:44]
e=a[13:19]
print(f'1.3 zmienna d ma wartosc {d}, a zmienna e {e}')

print(f'1.4 zmienna c ma wartosc {c.upper()}')
print(f'1.5 zmienna d ma wartosc {d.capitalize()}')

print(f'1.6 Nad {b}, {e} krzaczka miszkala {d} {c[0:9].upper()}!')

print(f'1.7. W zmiennej a wystepuje {a.count("k") + a.count("K")} liter k oraz {a.count("a") + a.count("A")} liter a')

z = input('podaj pierwsza liczbe ')
y = input('podaj druga liczbe ')

print(f'2. suma = {int(z) + int(y)}, \n roznica = {int(z) - int(y)}, \n pierwsza liczba do potegi drugiej = {int(z)**int(y)}, \n reszta z dzielenia przez 7 wartosci z potegi = {(int(z)**int(y))%7}, \n czesc calkowita z dzielenia iloczynu obu liczb przez 5 = {int((int(z)*int(y))/5)}')


print("3. litery z sa na pozycjach ", a.index('z'), a[6:].index('z')+6, a[9:].index('z')+9, a[23:].index('z')+23, a[26:].index('z')+26, a[34:].index('z')+34, a[42:].index('z')+42)

k = "Ssuhjpkiuengtyrrdsenmtfrespevfdsertn"
print(f"4. {k[0:1]}{k[2:3]}{k[5:6]}{k[9:10]}{k[15:16]}{k[20:21]}{k[27:28]}{k[35:36]}")