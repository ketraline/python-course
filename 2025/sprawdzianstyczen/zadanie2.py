people = [
    {"name": "John", "grades": [1, 2, 3, 4, 5]},
    {"name": "Jane", "grades": [1, 1, 1, 1, 1]},
    {"name": "Bob", "grades": [2, 3, 4, 5]},
    {"name": "Alice", "grades": [5, 3, 5]},
    {"name": "Charlie", "grades": [1, 2, 3, 4, 5]},
    {"name": "David", "grades": [2, 3, 1]},
    {"name": "Emily", "grades": [5, 5, 5, 5, 5]},
    {"name": "Frank", "grades": [3, 2, 1]},
    {"name": "Grace", "grades": [4, 3, 2, 1]},
    {"name": "Henry", "grades": [1]},
]

maxsrednia = 0.0
for i in range(len(people)):
    for j in range(i,len(people)):
        for k in range(j,len(people)):
            if i != j and j != k:
                gora = sum(people[i]['grades']) + sum(people[j]['grades']) + sum(people[k]['grades'])
                dol = len(people[i]['grades']) + len(people[j]['grades']) + len(people[k]['grades'])
                srednia = float(gora/dol)
                print(srednia, i, j, k)
                if srednia > maxsrednia:
                    maxsrednia = srednia

print(maxsrednia)

#zlozonosc czasowa O(n^3) i pamiec liniowa