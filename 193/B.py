N = int(input())

shops = []
for _ in range(N):
    A, P, X = map(int, input().split())
    shops.append([A, P, X])

shops = sorted(shops, key=lambda x: x[0])

possible = False
min_price = None

for shop in shops:
    A, P, X = shop[0], shop[1], shop[2]
    X -= A
    if X > 0:
        possible = True
        if min_price == None:
            min_price = P
        else:
            if min_price > P:
                min_price = P

if possible:
    print(min_price)
else:
    print(-1)
