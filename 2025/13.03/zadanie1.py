x = ["asjkdgh","isrksdbg","ueigr","hdjf","d","AD","A" "a", "ab","b","c","hdsk","uiosdfkgdfhse","anf","ien"]
def minimax(table):
    if len(table) == 0: raise Exception("Tablica musi miec conajmniej jeden element.")
    if len(table) == 1: return table[0], table[0]
    mini = [[table[0], len(table[0])]]
    maxi = [[table[0], len(table[0])]]
    for i in range(1,len(table)):
        if len(table[i]) > maxi[0][1]:
            maxi.clear()
            maxi = [[table[i], len(table[i])]]
        elif len(table[i]) == maxi[0][1]:
            maxi.append([table[i],len(table[i])])
            if maxi[0][0] >= maxi[1][0]:
                del(maxi[1])
            elif maxi[0][0] < maxi[1][0]:
                del(maxi[0])
        if len(table[i]) < mini[0][1]:
            mini.clear()
            mini = [[table[i], len(table[i])]]
        elif len(table[i]) == mini[0][1]:
            mini.append([table[i],len(table[i])])
            if mini[0][0] <= mini[1][0]:
                del(mini[1])
            elif mini[0][0] > mini[1][0]:
                del(mini[0])
    return mini[0][0], maxi[0][0]
print(minimax(x))
y = ["a", "aj","ad", "ay", "ac"]
print(minimax(y))
