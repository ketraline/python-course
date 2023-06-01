dec = int(input("podaj liczbe dziesietna "))
bina = bin(dec)[2:]
print(bina, type(bina))
x=0
a=0

for i in range(1,300):
    if bina[i-1:i] != bina[i:i+1]:
        print(bina[i:])
        x = x+1
    if x >= 2:
        a = a+1

print(x, a)