# April - Exercise on string editing.

a = "My jestesmy krasnoludki, hopsasa, hopsasa"

# 1.1 - b equals 8 symbols starting from the letter j
b = a[3:11]
print("1.1 "+"The variable b is equal = ", b)

# 1.2 - c equals 7 of the last symbols of the variable a
c = a[-7:]
print("1.2 "+"The variable c is equal = ", c)

# 1.3 - d equals the word "my" all in lowercase and e equals the word "krasnoludki" all in uppercase
d = a[0:2]
print("1.3 "+"The variable d is equal = ", d.lower())
e = a[12:23]
print("1.3 "+"The variable e is equal = ", e.upper())

# 1.4 Print e in all lowercase instead
print("1.4 "+"The variable e is equal = ", e.lower())

# 1.5 Print d with only the first letter in uppercase
print("1.5 "+"The variable d is equal = ", d.capitalize())

# 1.6 Print the sentence in variable a using the variables b,c,d,e
print("1.6 "+d+" "+b+" "+e+", "+c+", "+c)

# 2. We copy every third character of the variable I into the variable Wi, starting with a capital letter
# We copy every 4th character of the N variable into the Wn variable, starting with a capital letter
I="Rwdogrbnrimlnvsspponbnf"
N="gClkjrvrtudrusjfdoveseh"

Wi = I[::3]
Wn = N[1::4]
print(f"2. {Wi}{Wn}")

# 3. In the variable a from task 1, count the occurrences of the letter "s" and the letter "a"
print(f"3. In the variable a there is {a.count('s')} letters 's' and {a.count('a')} letters 'a'")

# 4. Remove all letters "x" from the variable p
p = "Pxrxogxxrxamxoxwaxnixxexx xtxo xcxzexxscx ixnfxoxxrxxmxaxtxyxkxxixxx."
print(f"4.", p.replace('x', ''))

# 5. Calculate for 2 numbers given in the console:
# a - sum
# b - difference
# c - power of three
# d - the remainder after dividing by 7
liczba1 = input("5. Input the first number: ")
liczba2 = input("Input the second number: ")
print(f"5. Sum = {int(liczba1) + int(liczba2)}, Difference = {int(liczba1) - int(liczba2)}, {liczba1} to the power of three = {int(liczba1)**3}, {liczba2} to the power of three = {int(liczba2)**3}, Remainder of {liczba1} after dividing by 7 = {int(liczba1)%7}, Remainder of {liczba2} after dividing by 7 = {int(liczba2)%7}")

# 6. Print colored text
A = '\033[1;33;46m'
B = '\033[1;30;41m'
C = '\033[1;31;44m'
re = '\033[0m'
print(C + "Programowanie" + re + " " + A + "jest" + re + " " + B + "SUPER" + re)
