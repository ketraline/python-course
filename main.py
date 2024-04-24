# x = int(input('podaj liczbe '))
# r = 0
# binarna = ''
# while x != 0:
#     r = x % 2
#     binarna = binarna + str(r)
#     x = x // 2
# print(binarna)

x = int(input('podaj liczbe '))
r = 0
last = -1
blocks = 0
while x != 0:
    r = x % 2
    if r == last:
        blocks += 1
    last = r
    x = x // 2
print(blocks)
