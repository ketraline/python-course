#1
def function(x):
    function.count +=1 #counts recursion 
    if x == 0:
        return 0
    else:
        return 2 + function(x//2)
        
function.count = 0
print(3, function(3), function.count)
function.count = 0
print(16, function(16),function.count)
function.count = 0
print(35, function(35), function.count)

#2 - Find min and max values when F(x) = 18
numbers = []
i=0
while i < 1000:
    if function(i) == 18:
        numbers.append(i)
    i+=1

print(min(numbers),max(numbers))