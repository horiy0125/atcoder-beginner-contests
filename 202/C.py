N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

_B = []
for c in C:
    if c <= N:
        _B.append(B[c-1])
    else:
        _B.append(-1)

max_a = max(A) + 1
max_b = max(_B) + 1

a_nums = [0] * max_a
b_nums = [0] * max_b

for a in A:
    a_nums[a] += 1

for b in _B:
    if b != -1:
        b_nums[b] += 1

answer = 0
min_num = min([max_a, max_b])
for n in range(min_num):
    answer += a_nums[n] * b_nums[n]

print(answer)
