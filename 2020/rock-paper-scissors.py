import random
lista = ["n", "p", "k"]

k = random.choice(lista)
g = input("podaj n,p,k: ")

if (k=="n" and g=="p") or (k=="p" and g=="k") or (k=="k" and g=="n"):

  print("komputer wybral: ",k)
  print("wygrał komputer :(")
  
elif (k=="n" and g=="n") or (k=="p" and g=="p") or (k=="k" and g=="k"):
    
    print("komputer wybral: ",k)
    print("remis")

else:
  print("komputer wybral: ",k)
  print("Wygrał-ś!!!")
