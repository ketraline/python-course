def dec_bin(n):
    binary=""
    if n == 0:
        return 0
    if n > 0:
        sign = 0
    else:
        sign = 1
    n = abs(n)
    while n != 0:
        binary = str(n%2) + binary
        n = n//2
    binary = str(sign) + binary
    return binary

def dec_hex(n):
    hexadecimal = []
    if n == 0:
        return 0
    while n != 0:
        hexadecimal = [n%16] + hexadecimal
        n = n//16
    for i in range(len(hexadecimal)):
        if hexadecimal[i] == 10: hexadecimal[i] = "A"
        if hexadecimal[i] == 11: hexadecimal[i] = "B"
        if hexadecimal[i] == 12: hexadecimal[i] = "C"
        if hexadecimal[i] == 13: hexadecimal[i] = "D"
        if hexadecimal[i] == 14: hexadecimal[i] = "E"
        if hexadecimal[i] == 15: hexadecimal[i] = "F"
    return "".join(hexadecimal)

print(dec_bin(10), dec_hex(10))