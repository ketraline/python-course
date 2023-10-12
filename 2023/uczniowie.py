uczniowie = []
oceny = []
def dodaj_oceny(uczen, ocena):
    uczen = input("podaj imie ucznia ")
    uczniowie.append(uczen)
    uczen = input("podaj ocene ucznia ")
    oceny.append(ocena)
    return True

def usun_oceny(uczen,ocena):
    uczen = input("podaj imie ucznia ")
    uczniowie.remove(uczen)
    uczen = input("podaj ocene ucznia ")
    oceny.remove(ocena)
    return True

def main():
    x = "*"
    y = "*"
    g = input("co chcesz zrobic? ")
    if g == "dodaj ocene":
        dodaj_oceny(x,y)
        main()
    elif g =="usun ocene":
        usun_oceny(x,y)
        main()
    elif g =="pokaz oceny":
        print(uczniowie,oceny)
        main()
    else:
        print("niepoprawne polecenie")
        main()

main()