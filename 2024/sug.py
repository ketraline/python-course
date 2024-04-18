tekst = "To jest przykladowy tekst do analizy. W tekscie tym wystepują rozne slowa, w tym rowniez powtarzajace się slowa. Analiza tekstu jest waznym elementem nauki programowania. Programowanie pozwala na przetwarzanie danych tekstowych w rozny sposob. Tekst ten zawiera rozne slowa, w tym slowo 'tekst' wystepujące kilkukrotnie."
lista = tekst.split(" ")
slowa = len(lista)
print(slowa)

niema = []
i=0

while i < 45:
    if lista[i] in niema:
        i += 1
    else:
        niema.append(lista[i])
        i+= 1
    
print(len(niema))
print(niema)