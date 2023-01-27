from sys import stdin

N, K = map(int, stdin.readline().split())
array = list(map(int, stdin.readline().split()))

if N == K:
    print(0)
elif K == 1:
    print(array[-1]-array[0])
else:
    gap = []
    for i in range(1, len(array)):
        gap.append([array[i]-array[i-1], i])

    gap.sort(key=lambda x: x[0], reverse=True)

    index = []
    index.append(N)
    for i in gap[:K-1]:
        index.append(i[1])
    index.sort()

    split = []
    n = 0
    for i in index:
        split.append(array[n:i])
        n = i

    cost = 0
    for i in split:
        cost += i[-1] - i[0]

    print(cost)
