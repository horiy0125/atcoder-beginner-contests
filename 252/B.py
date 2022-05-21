import sys

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

maximum = max(A)
answer = "No"
for n in range(N):
    if A[n] == maximum and n+1 in B:
        print("Yes")
        sys.exit()

print("No")
