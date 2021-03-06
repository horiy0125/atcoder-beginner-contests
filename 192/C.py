N, K = map(int, input().split())


def g1(n):
    return int(''.join(sorted(str(n), reverse=True)))


def g2(n):
    return int(''.join(sorted(str(n))))


def f(n):
    return g1(n) - g2(n)


for _ in range(K):
    N = f(N)

print(N)
