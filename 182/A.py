A, B = input().split()

A = int(A)
B = int(B)

max_follow = (2 * A) + 100
ans = max_follow - B
print(ans)
