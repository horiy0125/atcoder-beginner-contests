S = str(input())

answer = True

for index in range(len(S)):
    if index % 2 == 0:
        if not S[index].islower():
            answer = False
            break
    else:
        if S[index].islower():
            answer = False
            break

if answer:
    print('Yes')
else:
    print('No')
