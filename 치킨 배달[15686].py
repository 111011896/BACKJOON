from sys import stdin
from itertools import combinations

N, M = map(int, stdin.readline().split())

house = []
chicken = []
for i in range(1, N+1):
    line = list(map(int,stdin.readline().split()))
    for j in range(1, N+1):
        if line[j-1] == 1:
            house.append([i, j])
        elif line[j-1] == 2:
            chicken.append([i, j])

survive = combinations(chicken, M)

collection = []
for i in survive:
    chicken_distance = []
    for k in house:
        distances = []
        for j in i:
            distances.append(abs(j[0]-k[0])+abs(j[1]-k[1]))
        chicken_distance.append(min(distances))
    collection.append(sum(chicken_distance))

print(min(collection))
