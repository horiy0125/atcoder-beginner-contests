import itertools

N = int(input())
X, Y = map(int, input().split())

amount = []
takoyaki_sum = 0
taiyaki_sum = 0

for _ in range(N):
    A, B = map(int, input().split())
    amount.append([A, B])

    takoyaki_sum += A
    taiyaki_sum += B

dp = []
for _ in range(N):
    dp.append(-1)


def recursive(bento_id: int, takoyaki: int, taiyaki: int, bento_num: int) -> int:
    # if bento_id == len(amount):
    #     return bento_num

    if bento_id == len(amount):
        if takoyaki < X or taiyaki < Y:
            return 301
        else:
            return bento_num

    if takoyaki > 0 and taiyaki > 0:
        if dp[bento_id] == -1:
            result = min([
                recursive(bento_id + 1, takoyaki -
                          amount[bento_id][0], taiyaki - amount[bento_id][1], bento_num + 1),
                recursive(bento_id + 1, takoyaki, taiyaki, bento_num),
            ])

            dp[bento_id] = result
            return result
        else:
            return dp[bento_id]
    else:
        # return bento_num
        return recursive(bento_id + 1, takoyaki, taiyaki, bento_num)


if takoyaki_sum >= X and taiyaki_sum >= Y:
    print(recursive(0, X, Y, 0))
else:
    print(-1)
