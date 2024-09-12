# April - More string editing.

a = 'Nad rzeczka, opodal krzaczka miszkala Kaczka Dziwaczka.'

# 1.1 - b equals 7 symbols starting from the letter j
b=a[4:11]
print(f'1.1 zmienna b ma wartosc {b}')

# 1.2 - c equals 10 of the last symbols of the variable a
c=a[-10:]
print(f'1.2 zmienna c ma wartosc {c}')

# 1.3 - d equals the word "kaczka" and e equals the word "opodal"
d=a[38:44]
e=a[13:19]
print(f'1.3 zmienna d ma wartosc {d}, a zmienna e {e}')

# 1.4 Print c in all uppercase
print(f'1.4 zmienna c ma wartosc {c.upper()}')

# 1.5 Print d with only the first letter in uppercase
print(f'1.5 zmienna d ma wartosc {d.capitalize()}')

# 1.6 Print the sentence in variable a using the variables b,c,d,e but the word "dziwaczka" must be uppercase and the sentence must end with an exclamation mark
print(f'1.6 Nad {b}, {e} krzaczka mieszkala {d} {c[0:9].upper()}!')

# 1.7 In the variable a from task 1, count the occurrences of the letter "k" and the letter "a" regardless of capitalization
print(f'1.7. In the variable k there is {a.count("k") + a.count("K")} letters "k" and {a.count("a") + a.count("A")} letters "a"')

# 2. Calculate for 2 numbers given in the console:
# a - sum
# b - difference
# c - power of a to b
# d - the remainder after dividing by 7 of the value from c
# e - integer part from dividing the product of both variables by 5
z = input('Input the first number: ')
y = input('Input the second number: ')

print(f'2. Sum = {int(z) + int(y)}, \n Difference = {int(z) - int(y)}, \n a to the power of b = {int(z)**int(y)}, \n The remainder after dividing by 7 of the value from c = {(int(z)**int(y))%7}, \n integer part from dividing the product of both variables by 5 = {int((int(z)*int(y))/5)}')

# 3. Identify the positions of all the letters "z" in the variable "a" from task 1 (i must admit this solution is really dumb)
print("3. litery z sa na pozycjach ", a.index('z'), a[6:].index('z')+6, a[9:].index('z')+9, a[23:].index('z')+23, a[26:].index('z')+26, a[34:].index('z')+34, a[42:].index('z')+42)

# 4. Read the 7-letter word starting with the first character (i.e. "S") from the variable k
# We know that additional letters were added between the characters as follows:
# after the first letter of the searched word, 1 additional character, 2 characters were added after the second letter of the searched word, after three - three and so on
k = "Ssuhjpkiuengtyrrdsenmtfrespevfdsertn"
print(f"4. {k[0:1]}{k[2:3]}{k[5:6]}{k[9:10]}{k[15:16]}{k[20:21]}{k[27:28]}{k[35:36]}")