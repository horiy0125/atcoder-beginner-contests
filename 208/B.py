P = int(input())

coins = [1]

for i in range(2, 11):
    coins.append(coins[len(coins) - 1] * i)

coins.sort(reverse=True)

count = 0
for coin in coins:
    if P == 0:
        break
    if not P < coin:
        while P >= coin:
            P -= coin
            count += 1

print(count)
