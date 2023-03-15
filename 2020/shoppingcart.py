pr = print("""Witamy w sklepie “Office Depot”!
Wybierz z listy towar, który chcesz kupić
(wpisz numer i kliknij ENTER)""")
lista=["1. Długopis","2. Ołówek","3. Pióro","4. Koperta","5. Ryza papieru A4","6. Paczka spinaczy","7. Klej","8. “Post-it-notes”","9. Taśma klejąca"]
print("\n")
for element in lista:
  print(element)
  
numer = int(input("Numer towaru: "))
koszyk=[numer]
tn = input("Czy chcesz kontynuować zakupy? (T/N): ")

while numer > 0:
  if tn == "T" or "t":
    nr = input("Numer towaru: ")
    koszyk.append(nr)
    tn = input("Czy chcesz kontynuować zakupy? (T/N): ")
  else:
    break

print("Twój koszyk: ")
print(koszyk)
