A, B, C, K = map(int, input().split())

if K <= A:
    summary = K
else:
    require = K - A
    if require <= B:
        summary = A
    else:
        summary = A - (require - B) * 1

print(summary)
