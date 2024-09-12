n = int(input("podaj liczbe "))
if n==0: 
    print("0")
elif n==1:
    print("1")
else:
    k0 = 0
    k1 = 1
    for x in range(0, n-1):
        k2 = k0 + k1
        k0 = k1
        k1 = k2
print(k2)