import random

i = 0
string = ""
while i < 101:
    abnumer = random.randint(0,1)

    if abnumer == 0:
        ab = "A"
    else:
        ab = "B"

    ten = random.randint(1,10)
    string += ab * ten
    i += 1
print(string)