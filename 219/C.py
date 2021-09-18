X = input()
N = int(input())

d = []

for x in X:
    d.append(x)

names = []
max_length = 0

for n in range(N):
    name = input()
    names.append(name)

    if len(name) > max_length:
        max_length = len(name)

order_list = []

for name in names:
    order_num = ''

    for letter in name:
        order_num += str(d.index(letter) + 10)

    if len(order_num) != max_length * 2:
        order_num += '0' * (max_length * 2 - len(order_num))

    order_list.append([name, int(order_num)])

order_list.sort(key=lambda x: x[1])

for o in order_list:
    print(o[0])
