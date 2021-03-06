import math

N, M = input().split()
N, M = int(N), int(M)

if M == 0:
    answer = 1
elif M == N:
    answer = 0
else:
    A = input().split()
    A.append(0)

    for i in range(M):
        A[i] = int(A[i])

    A.sort()
    A.append(N+1)

    x = []

    for i in range(len(A) - 1):
        result = A[i+1] - A[i]
        if result > 1:
            x.append(result - 1)

    x.sort()

    answer = 0

    for i in x:
        answer += math.ceil(i / min(x))

print(answer)
