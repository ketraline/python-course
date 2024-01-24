plik = open("2024/test/zad2/liczby.txt", "r")
tekst = plik.read()
tekst = tekst.split('   ')
tekst.pop()
tekst = list(map(int, tekst))
# 2a
print("max", max(tekst))
print("min", min(tekst), "\n")
wym = open("wymnik2.txt","a")
wym.write(f"2a: max {max(tekst)} min {min(tekst)} \n")

# 2b
print("liczby ktore sie powtarzaja\n")
lista = [] # empty list to hold unique elements from the list
duplikaty = [] # empty list to hold the duplicate elements from the list
i = 0
for i in tekst:
    if i not in lista:
        lista.append(i)
    else:
        duplikaty.append(i)
print(duplikaty, "\n")
wym.write(f"2b: {duplikaty}\n")

# 2c
print("liczby podzielne przez 13\n")
podzielne = []
i = 0
while i < 1000:
    if tekst[i]%13 == 0:
        podzielne.append(tekst[i])
    i += 1
print(podzielne, "\n")
wym.write(f"2c: {podzielne}\n")

# 2d
print("posortowane liczby\n")
podzielne.sort()
print(podzielne)
g = open("liczby13.txt", "a")
g.write(str(podzielne))

# 2e
jedynki = []
rowno = []

for i in lista:
  value = bin(i)
  if value.count('0') == 1:
    jedynki.append(i)
  if value.count('0')-1 == value.count('1'):
    rowno.append(i)
print(jedynki)
print(rowno)
wym.write(f"2e: jedynki {jedynki}, po rowno {rowno}")

#2f
suma11 = 0
suma13 = 0
suma15 = 0
suma17 = 0
suma19 = 0

for i in range(10, 20):
  if i%2 != 0:
    for o in range(len(lista)):
      if lista[o]%i == 0:
        if i == 11:
          suma11 += 1
        if i == 13:
          suma13 += 1
        if i == 15:
          suma15 += 1
        if i == 17:
          suma17 += 1
        if i == 19:
          suma19 += 1

lista_suma = [suma11, suma13, suma15, suma17, suma19]
dziel = 0
for z in range(len(lista_suma)):
  if lista_suma[z] == max(lista_suma):
    dziel = 10 + 2*z + 1
    print("podzielnik z największą wielokrotnością: ", dziel)
lista_dziel=[]
for i in range(len(lista)):
  if lista[i]%dziel == 0:
    lista_dziel.append(lista[i])

f = open("liczby_w.txt","a")
f.write(f"{dziel}, {lista_dziel}")