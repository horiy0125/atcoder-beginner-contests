S = input()

if S[1:2] == 'S':
    if 'R' in S:
        print(1)
    else:
        print(0)
else:
    if not 'S' in S:
        print(3)
    else:
        if S == 'SRS':
            print(1)
        else:
            print(2)
