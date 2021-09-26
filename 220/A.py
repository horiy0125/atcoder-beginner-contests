A, B, C = map(int, input().split())

answer = -1
for i in range(A, B+1):
    if i % C == 0:
        answer = i

print(answer)
