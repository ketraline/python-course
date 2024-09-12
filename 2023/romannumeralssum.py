# April - Calculate the sum of two roman numerals (no bigger than MMM/3000)

rzymska1 = input("Input the first roman numeral: ")
if rzymska1 == "I":
    rzymska1 = 1
elif rzymska1 == "V":
    rzymska1 = 5
elif rzymska1 == "X":
    rzymska1 = 10
elif rzymska1 == "L":
    rzymska1 = 10
elif rzymska1 == "C":
    rzymska1 = 100
elif rzymska1 == "D":
    rzymska1 = 500
elif rzymska1 == "M":
    rzymska1 = 1000
else:
    print("That's not a roman numeral")
rzymska2 = input("Input the first roman numeral: ")
if rzymska2 == "I":
    rzymska2 = 1
    print(rzymska1 + rzymska2)
elif rzymska2 == "V":
    rzymska2 = 5
    print(rzymska1 + rzymska2)
elif rzymska2 == "X":
    rzymska2 = 10
    print(rzymska1 + rzymska2)
elif rzymska2 == "L":
    rzymska2 = 10
    print(rzymska1 + rzymska2)
elif rzymska2 == "C":
    rzymska2 = 100
    print(rzymska1 + rzymska2)
elif rzymska2 == "D":
    rzymska2 = 500
    print(rzymska1 + rzymska2)
elif rzymska2 == "M":
    rzymska2 = 1000
    print(rzymska1 + rzymska2)
else:
    print("That's not a roman numeral")