N = int(input())

A = input().split()
B = input().split()

result = 0

for i in range(N):
    result += int(A[i]) * int(B[i])

if result == 0:
    print('Yes')
else:
    print('No')
