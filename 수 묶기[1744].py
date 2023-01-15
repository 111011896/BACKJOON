from sys import stdin

N = int(stdin.readline())
neg = []
pos = []
for i in range(N):
    line = int(stdin.readline())
    if line <= 0:
        neg.append(line)
    else:
        pos.append(line)

neg.sort()
pos.sort(reverse=True)
len_neg = len(neg)
len_pos = len(pos)

result = 0
i = 0
while True:
    if len_neg % 2 == 0:
        if i >= len_neg:
            break
        result += neg[i] * neg[i+1]
        i += 2
    else:
        if i == len_neg-1:
            result += neg[i]
            break
        elif i >= len_neg:
            break
        result += neg[i] * neg[i+1]
        i += 2

j = 0
while True:
    if len_pos % 2 == 0:
        if j == len_pos-1:
            result += pos[j]
            break
        elif j >= len_pos:
            break
        if pos[j] in [0, 1]:
            result += pos[j]
            j += 1
        else:
            if pos[j+1] not in [0, 1]:
                result += pos[j] * pos[j+1]
                j += 2
            else:
                result += pos[j]
                j += 1
    else:
        if j == len_pos-1:
            result += pos[j]
            break
        elif j >= len_pos:
            break
        if pos[j] in [0, 1]:
            result += pos[j]
            j += 1
        else:
            if pos[j + 1] not in [0, 1]:
                result += pos[j] * pos[j + 1]
                j += 2
            else:
                result += pos[j]
                j += 1

print(result)
