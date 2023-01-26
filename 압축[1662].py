from sys import stdin

S = list(stdin.readline().rstrip())

def findFB(S):
    F = 0
    B = 0
    for i in range(len(S)):
        if S[i] == "(":
            F += 1
        elif S[i] == ")":
            B += 1
        if F != 0 and B != 0:
            if F == B:
                return i

def compact(S):
    n = 0
    i = 0
    while True:
        if i == len(S):
            return n
        if S[i].isdigit():
            n += 1
            i += 1
        elif S[i] == "(":
            n -= 1
            n += int(S[i-1]) * compact(S[i+1:findFB(S)])
            del S[i:findFB(S)+1]

print(compact(S))
