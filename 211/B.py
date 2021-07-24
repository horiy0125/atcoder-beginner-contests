c = [False] * 4

for _ in range(4):
    S = input()

    if S == 'H':
        c[0] = True
    elif S == '2B':
        c[1] = True
    elif S == '3B':
        c[2] = True
    elif S == 'HR':
        c[3] = True

if False in c:
    print('No')
else:
    print("Yes")
