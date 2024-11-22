godzina = int(input("podaj godzinę (bez minut) "))
if godzina >= 5 and godzina < 9:
    print("jest rano")
elif godzina >= 9 and godzina <=18:
    print("jest dzień")
elif godzina > 18 and godzina < 23:
    print("jest wieczór")
else:
    print("jest noc")
