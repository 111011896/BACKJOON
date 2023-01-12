from sys import stdin

N = int(stdin.readline())
array = [int(stdin.readline()) for i in range(N)]

result = 0
while True:
    array.sort()
    pop_left = array.pop(0)
    if not array:
        print(result)
        break
    array[0] += pop_left
    result += array[0]
