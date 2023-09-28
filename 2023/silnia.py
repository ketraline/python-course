def ciag():
    x = int(input("podaj liczbe do ciagowania "))
    n = (x*(x+1))/2
    print(int(n))
    ciag()

ciag()