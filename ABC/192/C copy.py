import sys
sys.setrecursionlimit(1000000)


def f(number, K, now):

    g2 = int(''.join(sorted(str(number))))
    g1 = int(''.join(sorted(str(number), reverse=True)))

    now += 1
    answer = int(g1) - int(g2)
    if now == K:
        return answer
    else:
        return f(answer, K, now)


N, K = map(int, input().split())

now = 0
print(f(N, K, now))
