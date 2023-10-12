
def fib(n):
    if n==0: 
        print("0")
    if n==1:
        print("1")
    k0 = 0
    k1 = 1
    i = range(2, n)
    for x in i:
        m = k0 + k1
        print(m)
        k1 = k0
        k0 = m
        x+= 1
    fib(n)
n = int(input("podaj liczbe "))
fib(n)
