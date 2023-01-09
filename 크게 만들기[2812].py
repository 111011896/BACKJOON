from sys import stdin

N, K = map(int, stdin.readline().split())
array = list(map(int, stdin.readline().rstrip()))

stack = []
n = 0
for i in range(N):
    while True:
        pivot = array[i]
        if not stack:
            stack.append(pivot)
            break
        elif stack[-1] >= pivot:
            stack.append(pivot)
            break
        else:
            if n < K:
                stack.pop()
                n += 1
            else:
                stack.append(pivot)
                break

if n != K:
    for i in range(K-n):
        stack.pop()

if not stack:
    stack.append(0)

for i in stack:
    print(i, end='')
