x =input ("podaj liczbe ")
if x.isdigit(): 
    x = int(x)
    if x >= 0 | x <= 20:
        silnia = 1
        i = 1
        while i <= x:
            silnia = silnia*i
            i+=1
        print(silnia)
    else:
        print("liczba jest za duza/mala")
else:
    print("to nie jest liczba")