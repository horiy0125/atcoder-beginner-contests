A, B = map(int, input().split())

K = A + B

if K >= 15 and B >= 8:
    answer = 1
elif K >= 10 and B >= 3:
    answer = 2
elif K >= 3:
    answer = 3
else:
    answer = 4

print(answer)
