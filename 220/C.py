from decimal import Decimal

N = int(input())
A = list(map(int, input().split()))
X = int(input())

summary = 0
for a in A:
    summary += a


count = int(Decimal(str(X)) / Decimal(str(summary)))
result = summary * count

answer = N * count
_count = 0
while result <= X:
    if result + A[_count] > X:
        break
    else:
        result += A[_count]
        _count += 1

answer += _count + 1
print(answer)
