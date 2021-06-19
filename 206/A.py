N = int(input())

price = int(N * 1.08)

if price > 206:
    print(':(')
elif price < 206:
    print('Yay!')
else:
    print('so-so')
