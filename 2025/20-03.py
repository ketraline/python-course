# 1. Przeanalizuj poniższy kod.
# Na podstawie analizy zmień ich nazwy na opisowe - tzn. takie, które określać będą cel danej funkcji.
# W second_func popraw wiadomości "first exception" i "second exception"

import time

def randomInRange(a, b):
    t = time.time_ns() #czas w nanosekundach od jan 1 1970
    mixed_number = (t * 73 + 41) 
    return a + (mixed_number % (b - a + 1)) #losowa liczba z zakresu <a,b>

def checkIfInt(a,b):
    if type(a) is not int:
        raise Exception(f"Argument a has to be an integer")

    if type(b) is not int:
        raise Exception(f"Argument b has to be an integer")

    return randomInRange(a, b)


for i in range(10):
    print(f"{i} {checkIfInt(78.88, 10001)}")