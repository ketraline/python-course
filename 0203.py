imie = "jan"

#false
print(bool(""))
#true
print(bool("tomek"))

#imie jest truthy
if imie:
    print("imie istnieje")

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Unsuccessful")

for x in range(5):
    for y in range(5):
        print(f"({x}, {y})")

count = 0
for x in range(10):
    if x%2==0:
        print(x)
        count = count + 1
print(count, "liczb parzystych")

def nazwafunkcji():
    print("ababobasdof")

print(nazwafunkcji())