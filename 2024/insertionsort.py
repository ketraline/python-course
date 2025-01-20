lista = [5,2,3,6,4,1]
lista2 = ['x', 'a', 'ab','z', 'f', 'afdg']
lista3 = [6,2,"az",8,"abbv","ab","ba",'a',34,"23","ac",'d','n',9,'z']

def insertionsort(n):
    i=1
    for i in range(len(n)):
        for j in range(i,len(n)):
            if n[i]>n[j]:
                znak = n[i]
                n[i] = n[j]
                n[j] = znak
    i=0
    for i in range(len(n)):
        if type(n[i]) == str:
            for j in range(i-1,len(n)):
                if len(n[j])<len(n[i]):
                    print(n, i, j, len(n[i]), len(n[j]))
                    znak = n[i]
                    n.remove(znak)
                    n.append(znak)
                    j=i-1
    return(n)

def multitypeinsertionsort(n):
    string = []
    integer = []
    for i in range(len(n)):
        if type(n[i]) == str:
            if n[i].isnumeric() == True:
                integer.append(int(n[i]))
            else:
                string.append(n[i])
        else:
            integer.append(n[i])
    string = insertionsort(string)
    integer = insertionsort(integer)
    return(integer + string)

print(multitypeinsertionsort(lista3))