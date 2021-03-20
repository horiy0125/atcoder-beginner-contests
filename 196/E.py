N = int(input())

A = []
T = []

for n in range(N):
    a, t = map(int, input().split())
    A.append(a)
    T.append(t)

Q = int(input())


def f1(x: int, ai: int) -> int:
    return x + ai


def f2(x: int, ai: int) -> int:
    return max([x, ai])


def f3(x: int, ai: int) -> int:
    return min([x, ai])


X = list(map(int, input().split()))

for q in range(Q):
    x = X[q]
    for n in range(N):
        if T[n] == 1:
            x = f1(x, A[n])
        elif T[n] == 2:
            x = f2(x, A[n])
        else:
            x = f3(x, A[n])
    print(x)
