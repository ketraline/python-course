import math

name = "kajshnkjdank aksghfkhd "
print(name.upper()) #robi caps lock
print(name.lower()) #robi lowercase
print(name.title()) #duze litery na poczatku wyrazu
print(name.find("sh")) #szuka frazy
print(name.replace("n","d")) #zamienia znaki
print("kajshnkjdank" in name) #w zmiennej
print("kajshnkjdank" not in name) #nie w zmiennej
print(10**3) #10 do potegi 3
print(abs(-2.9)) #odwrotnosc
print(math.ceil(2.2)) #zaokragla do gory
print("apple" > "bag") #liczy sie tylko 1 litera
print("bag" == "BAG") #lower i uppercase sa rozne
print(name)

print("whats the temperature: ")
temperature = int(input())
if temperature > 30:
    print("its really warm")
elif temperature <10:
    print("its cold")
else:
    print("its average")

print("whats your age")
age = int(input())
if age >= 18:
    print("you can buy alcohol")
else:
    print("you can buy cola")

for zmienna in range(3):
    print(zmienna)