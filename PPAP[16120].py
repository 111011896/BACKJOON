from sys import stdin

TEXT = stdin.readline().rstrip()

stack = []
for i in range(len(TEXT)):
    while True:
        if not stack:
            stack.append(TEXT[i])
            break
        elif len(stack) < 4:
            stack.append(TEXT[i])
            break
        else:
            if stack[-4:] == ['P','P','A','P']:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('P')
            else:
                stack.append(TEXT[i])
                break

if stack == ['P','P','A','P']:
    stack = ['P']

if stack == ['P']:
    print('PPAP')
else:
    print('NP')
