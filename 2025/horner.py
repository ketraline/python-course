def horner(A, P):
    if P == 10: return A
    if type(A) != str: raise Exception("First argument must be str.")
    W = 0
    for i in A:
        if i in "ABCDEFGHIJ":
            if P < 11: raise Exception(f"Letter {i} cannot be converted in system {P}")
            j = "ABCDEFGHIJ".index(i)
            W = W * P + int(translate[j][1])
        else:
            W = W * P + int(i)
    return W
translate = [['A',10],['B',11],['C',12],['D',13],['E',14],['F',15],['G',16],['H',17],['I',18],['J',19]]
print(horner("ABCDEFGHIJ",20))
print(int("ABCDEFGHIJ",20))
print(horner(10, 10))
