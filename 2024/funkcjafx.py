def function(x):
    if x == 0:
        return 0
    else:
        return 2 + function(x//2)

print(function(3))
