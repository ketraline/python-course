z = input("podaj liczbe po RZYMSKU: ")

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
sum = 0

i = z.find("I")
v = z.find("V")
x = z.find("X")
l = z.find("L")
c = z.find("C")
m = z.find("M")
d = z.find("D")

sum = I*z.count("I") + V*z.count("V") + X*z.count("X") + L*z.count("L") + C*z.count("C") + D*z.count("D") + M*z.count("M")

if i == v-1 & i != 0:
    sum = sum - 2
if x == l-1 & i != 0:
    sum = sum - 20
if x == c-1 & i != 0:
    sum = sum - 20
if c == d-1 & i != 0:
    sum = sum - 200
if c == m-1 & i != 0:
    sum = sum - 200
print(sum)
