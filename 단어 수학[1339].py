from sys import stdin

N = int(stdin.readline())
words = [stdin.readline().rstrip() for i in range(N)]

order = {}
for i in range(10):
    try:
        dic = {}
        for word in words:
            for j in range(len(word)):
                pivot = word[j]
                if pivot not in order:
                    if pivot not in dic:
                        dic[pivot] = (9-i)*(10**(len(word)-j-1))
                    else:
                        dic[pivot] += (9-i)*(10**(len(word)-j-1))
                else:
                    pass
        for k, v in dic.items():
            if max(dic.values()) == v:
                order[k] = 9-i
                break
    except:
        break

sum = 0
for word in words:
    result = ''
    for i in word:
        result += str(order[i])
    sum += int(result)

print(sum)
