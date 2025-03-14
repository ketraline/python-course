"""
2. W słowniku zdania znajdziesz budulce zdań. 

Przyjmujemy, że zdanie sensowne to takie, które:

Zawiera co najmniej jeden podmiot.

Zawiera dokładnie jedno orzeczenie.

Może zawierać spójniki, ale tylko do łączenia podmiotów (nie mogą łączyć orzeczeń).

Może składać się tylko z podmiotu i orzeczenia, spójnik jest opcjonalny.

Twoim zadaniem jest znalezienie wszystkich kombinacji budulców zdań pozwalających na otrzymanie zdania sensownego.
Zapisz listę tak utworzonych zdań sensownych do pliku razem z ich liczbą.
"""
zdania = {
    "podmioty": ["Ala", "kot", "pies"],
    "spójniki": ["i", "oraz", "ale"],
    "orzeczenia": ["śpi", "biegnie", "je"]
}

sensowne = []
zdania["spójniki"].append(" ")
for a in range(len(zdania["podmioty"])):
    for b in range(len(zdania["spójniki"])):
        for c in range(len(zdania["podmioty"])):
            for d in range(len(zdania["spójniki"])):
                for e in range(len(zdania["podmioty"])):
                    for f in range(len(zdania["orzeczenia"])):
                        if zdania["spójniki"][b] == " ":
                            sensowne.append(f"{zdania['podmioty'][a]} {zdania['orzeczenia'][f]}")
                        elif zdania["spójniki"][d] == " " and  a != c and b != d:
                            sensowne.append(f"{zdania['podmioty'][a]} {zdania['spójniki'][b]} {zdania['podmioty'][c]} {zdania['orzeczenia'][f]}")
                        elif a != c and c != e and a != e and b != d:
                            sensowne.append(f"{zdania['podmioty'][a]} {zdania['spójniki'][b]} {zdania['podmioty'][c]} {zdania['spójniki'][d]} {zdania['podmioty'][e]} {zdania['orzeczenia'][f]}")
print(*set(sensowne), sep = "\n")
print(len(set(sensowne)))
