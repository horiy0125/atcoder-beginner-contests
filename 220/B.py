K = int(input())
A, B = map(str, input().split())


def base_n_to_10(X, n):
    out = 0
    for i in range(1, len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out


_A = base_n_to_10(A, K)
_B = base_n_to_10(B, K)

print(_A * _B)
