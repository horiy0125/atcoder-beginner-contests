N, M = map(int, input().split())

stores = []

for n in range(N):
    A, B = map(int, input().split())
    stores.append([A, B])

stores.sort(key=lambda x: x[0])

budget = 0

for s in stores:
    price = s[0]
    stocks = s[1]

    if stocks >= M:
        budget += price * M
        M = 0
    else:
        budget += price * stocks
        M -= stocks

    if M == 0:
        break

print(budget)
