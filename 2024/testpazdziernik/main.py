file = open("2024\\testpazdziernik\dane.txt")
liczby = file.read()
liczby = liczby.splitlines()
liczby.pop()

#1.1
szczesliwe = []
for i in range(0,10000):
    if i % 2 != 0:
        szczesliwe.append(i)
szczesliwe3 = []
while i in range(1, len(szczesliwe)):
    szczesliwe.pop(i)
    i =+2 
print(szczesliwe)

#2.1
palindrom = []
for i in range(32,63):
    if str(i)[0] == str(i)[1]:
        binarna=""
        a = i
        while a != 0:
            binarna = str(a%2) + binarna
            a = a//2
        if binarna[0] == binarna[5]:
            if binarna[1] == binarna[4]:
                if binarna[2] == binarna[3]:
                    palindrom.append(binarna)
print(palindrom)
file = open("wyniki2_2.txt","w")
file.write(f"2.1 Palindromy: {palindrom}")

#2.2
palindrom = []
palindromsuma = 0
for i in range(0,1000000):
    if i < 10:
        palindromsuma += i
    else:
        if str(i) == str(i)[::-1]:
            binarna=""
            a = i
            while a != 0:
                binarna = str(a%2) + binarna
                a = a//2
            if binarna == binarna[::-1]:
                palindrom.append(binarna)
                palindromsuma += i
print(palindrom,palindromsuma)
file = open("wyniki2_2.txt","w")
file.write(f"2.2 Suma: {palindromsuma}")