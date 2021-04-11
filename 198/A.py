N = int(input())

if N == 0 and N == 1:
    print(0)
elif N == 2:
    print(1)
else:
    N -= 2
    print(N + 1)
