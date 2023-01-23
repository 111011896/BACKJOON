from sys import stdin

N = int(stdin.readline())
sets = [list(map(int, stdin.readline().split())) for i in range(N)]
sets.sort(key=lambda x:x[0])

cnt = {}
for d, w in sets:
    if d not in cnt:
        cnt[d] = 1
    else:
        cnt[d] += 1

sorted_cnt = sorted(cnt.items())

idx = 0
cnt_sum = 0
que = []
for d, c in sorted_cnt:
    idx += c
    cnt_sum += c
    if cnt_sum <= d:
        for d1, w in sets[idx-c:idx]:
            que.append(w)
    else:
        gap = cnt_sum - d
        for d2, w in sets[idx-c:idx]:
            que.append(w)
        que.sort()
        que = que[gap:]
        cnt_sum -= gap

print(sum(que))
