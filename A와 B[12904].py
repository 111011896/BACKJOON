from sys import stdin

S = stdin.readline().rstrip()
T = stdin.readline().rstrip()

while True:
    if len(T) == len(S) and T != S:
        print(0)
        break
    elif T == S:
        print(1)
        break
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[::-1][1:]
