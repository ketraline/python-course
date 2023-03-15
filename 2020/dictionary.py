p = open("slownik.csv", "r")
slownik = {}

for linijka in p:
  linijka = linijka.strip()
  lista = linijka.split(",")
  
  slownik[lista[0]] = lista[1]
  
licznik = 0

for key in slownik:
  print(key)
  
  odp=input(">")

  if odp == slownik[key]:
    print("dobrze :] \n")
    licznik = licznik + 1
 
  else:
    print("źle :[ \n")
  


print("poprawnych:" , licznik)
