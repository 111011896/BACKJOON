from sys import stdin
from itertools import product

N = stdin.readline().rstrip()
M = int(stdin.readline())

if M != 10:
    if M != 0:
        Broken = list(map(int, stdin.readline().split()))
    else:
        Broken = []

    Not_Broken = []
    for i in range(10):
        if i not in Broken:
            Not_Broken.append(i)

    nPr = list(product(Not_Broken, repeat=len(N)))

    nPr_int = []
    for i in nPr:
        tem = ''
        if i[0] != 0:
            for j in i:
                tem += str(j)
            nPr_int.append(int(tem))
        elif i[0] == 0 and len(i) == len(N):
            nPr_int.append(0)

    min_gap = []
    for i in nPr_int:
        min_gap.append([abs(int(N)-i), i])

    candi1 = min(min_gap)[1]

    new_Not_Broken = []
    if 0 in Not_Broken:
        new_Not_Broken = Not_Broken[1:]
    else:
        new_Not_Broken = Not_Broken

    if new_Not_Broken:
        if len(N) > 1:
            if 0 in Not_Broken:
                candi2 = int(str(min(new_Not_Broken)) + '0' * (len(N)))
            else:
                candi2 = int(str(min(new_Not_Broken)) * (len(N) + 1))
            candi3 = int(str(max(new_Not_Broken)) * (len(N)-1))

            final_candi = min([abs(int(N)-candi1), candi1], [abs(int(N)-candi2), candi2], [abs(int(N)-candi3), candi3])[1]

            min_cnt = min(len(str(final_candi))+abs(int(N)-final_candi), abs(100-int(N)))
            print(min_cnt)
        else:
            if 0 in Not_Broken:
                candi2 = int(str(min(new_Not_Broken)) + '0' * (len(N)))
            else:
                candi2 = int(str(min(new_Not_Broken)) * (len(N) + 1))

            final_candi = min([abs(int(N) - candi1), candi1], [abs(int(N) - candi2), candi2])[1]

            min_cnt = min(len(str(final_candi)) + abs(int(N) - final_candi), abs(100 - int(N)))
            print(min_cnt)
    else:
        min_cnt = min(len(str(candi1))+abs(int(N)-candi1), abs(100-int(N)))
        print(min_cnt)
else:
    Broken = list(map(int, stdin.readline().split()))
    min_cnt = abs(100-int(N))
    print(min_cnt)
