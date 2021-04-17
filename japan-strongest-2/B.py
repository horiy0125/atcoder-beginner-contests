N, M = map(int, input().split())

A = input().split()
B = input().split()

for n in range(N):
    A[n] = int(A[n])

for m in range(M):
    B[m] = int(B[m])

_A = set(A)
_B = set(B)


all = _A | _B

only_B = all - _A
only_A = all - _B

answer = only_A | only_B

for a in answer:
    print(a, end=" ")
