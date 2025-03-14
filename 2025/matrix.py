words = [["abecadło", "haft", "brzoza", "Ignacy", "encefalopatia"],
["zgryz", "cyrk", "ul", "brom", "dziękować"],
["ruszt", "litr", "wóz", "barman", "lalka"],
["breja", "cyna", "tarka", "lilia", "nigdy"],
["trzeć", "nie", "osioł", "piżmo", "cynk"]]

#1. Znajdź wszystkie pary ciągów znaków, których suma długości daje 10.
slowa = []
for i in range(len(words)):
    for j in range(len(words[i])):
        slowa.append(words[i][j])
pary = []
for i in range(len(slowa)):
    for j in range(i+1,len(slowa)):
        if len(slowa[i]) + len(slowa[j]) == 10:
            pary.append([slowa[i], slowa[j]])
print(pary, len(pary))

#2. Znajdź wszystkie pary ciągów znaków, których suma długości jest mniejsza niż 10.
pary = []
for i in range(len(slowa)):
    for j in range(i+1,len(slowa)):
        if len(slowa[i]) + len(slowa[j]) < 10:
            pary.append([slowa[i], slowa[j]])
print(pary, len(pary))