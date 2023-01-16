from sys import stdin

N = int(stdin.readline())
K = int(stdin.readline())
coord = list(map(int, stdin.readline().split()))
coord.sort()

if N > K:
    gaps = []
    for i in range(1, N):
        gaps.append([coord[i]-coord[i-1], i])

    gaps.sort(key=lambda x: x[0], reverse=True)

    index = [0]
    for i in range(K-1):
        index.append(gaps[i][1])

    index.sort()
    index.append(len(coord))

    result = 0
    for i in range(1, K+1):
        result += coord[index[i]-1] - coord[index[i-1]]

    print(result)
else:
    print(0)
