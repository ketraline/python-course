z1 = input("podaj pierwsza liczbe po RZYMSKU (z duzych liter): ")
z2 = input("podaj druga liczbe po RZYMSKU (z duzych liter): ")

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
sum1 = 0
sum2 = 0

i = z1.find("I") and z2.find("I")
v = z1.find("V") and z2.find("V")
x = z1.find("X") and z2.find("X")
l = z1.find("L") and z2.find("L")
c = z1.find("C") and z2.find("C")
m = z1.find("M") and z2.find("M")
d = z1.find("D") and z2.find("D")

sum1 = I*z1.count("I") + V*z1.count("V") + X*z1.count("X") + L*z1.count("L") + C*z1.count("C") + D*z1.count("D") + M*z1.count("M")
sum2 = I*z2.count("I") + V*z2.count("V") + X*z2.count("X") + L*z2.count("L") + C*z2.count("C") + D*z2.count("D") + M*z2.count("M")
if sum1 == 0 or sum2 == 0:
    print("to nie jest liczba rzymska")
else:
    print(sum1+sum2)
