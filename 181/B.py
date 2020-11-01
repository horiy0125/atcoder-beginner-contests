N = int(input())

count = 0

for index in range(N):
    A, B = input().split()
    A = int(A)
    B = int(B)
    total = B * (B + 1) / 2
    result = total - A * (A - 1) / 2
    count += result

print(int(count))
