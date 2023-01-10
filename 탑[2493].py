from sys import stdin

N = int(stdin.readline())
array = list(map(int, stdin.readline().split()))[::-1]

answer = [0] * N
stack = []
for i in range(N):
    while True:
        pivot = array[i]
        if not stack:
            stack.append([pivot, i])
            break
        elif stack[-1][0] > pivot:
            stack.append([pivot, i])
            break
        else:
            idx = stack.pop()[1]
            answer[idx] = N-i

for i in answer[::-1]:
    print(i, end=' ')
