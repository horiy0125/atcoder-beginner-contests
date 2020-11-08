N = int(input())
A = input().split()

for i in range(len(A)):
    A[i] = int(A[i])

ints = []
k = 2

while k <= 1000:
    ints.append(k)
    k += 1

gcd = [0] * 1001

for k in ints:
    for a in A:
        if a % k == 0:
            gcd[k] += 1

maxgcd = max(gcd)
ans = gcd.index(maxgcd)
print(ans)
