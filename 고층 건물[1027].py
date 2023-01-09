n = int(input(""))
x = input("")
x_list = [int(i) for i in x.split()]
sets = []

for i in range(n):
    num = 0
    for j in range(n):
        if i < j:
            slope = (x_list[j]-x_list[i])/(j-i)
            set = 0
            for k in range(i+1, j):
                function = slope*(k-i)+x_list[i]
                if function <= x_list[k]:
                    break
                else:
                    set += 1
            if set == len(range(i+1, j)):
                num += 1
        elif j < i:
            slope = (x_list[i]-x_list[j])/(i-j)
            set = 0
            for k in range(j+1, i):
                function = slope*(k-i)+x_list[i]
                if function <= x_list[k]:
                    break
                else:
                    set += 1
            if set == len(range(j+1, i)):
                num += 1
        else:
            pass
    sets.append(num)

print(max(sets))
