lista = [5,2,3,6,4,1]
lista2 = ['x', 'a', 'f']
lista3 = [6,2,8,'a',3,'d','n',9,'z']

def insertionsort(n):
    i = 1
    while i < len(n):
        if n[i-1]>n[i]:
            znak = n[i-1]
            n.remove(znak)
            n.append(znak)
            i = 1
        else:
            i+=1
    return(n)

def bubblesort(n):
    i = 1
    sort = 0
    swapped = True
    for a in range(len(n)):
        if n[i-1]<n[i]:
            swapped = False
    if swapped == False: return(n)
    for i in range(len(n)-sort):
        znak = max(n[:len(n)-sort])
        n.remove(znak)
        n.append(znak)
        sort+=1
    n = n[::-1]
    return(n)

def multitypebubblesort(n):
    string = []
    integer = []
    for i in range(len(n)):
        if type(n[i]) == str:
            string.append(n[i])
        else:
            integer.append(n[i])
    string = bubblesort(string)
    integer = bubblesort(integer)
    return(string + integer)

def mixbubblesort(n):
    integer = []
    for i in range(len(n)):
        if type(n[i]) == int:
            n[i] = str(n[i])
            integer.append(n[i])
    bubblesort(n)
    n = n[::-1]
    for i in range(len(integer)):
        if n[i] in integer:
            n[i] = int(n[i])
    return(n)

print(mixbubblesort(lista3))