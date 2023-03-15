litery = "ABCDEFGHIJKLMNOPRSTUWXYZabcdefghijklmnoprstuwxyzĄĆĘŁÓŚŹŻąćęłóśźż"

p1 = open("tekst_in.txt", "r")
p2 = open("tekst_out.txt", "w")

tekst_in = p1.read()
tekst_out = ""

for litera in tekst_in:
  
  if litera not in litery:
    tekst_out = tekst_out + litera
    
  else:
    indeks_1 = litery.find(litera)
    indeks_2 = indeks_1 + 3
  
  if indeks_2 > 63:
    indeks_2 = indeks_2 + 64
    
  tekst_out = tekst_out + litery[indeks_2]

p2.write(tekst_out)
print("zapisano plik")

p1.close()
p2.close()
