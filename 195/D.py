import itertools

N, M, Q = map(int, input().split())

baggages = []

for index in range(N):
    W, V = map(int, input().split())
    baggages.append([W, V])

size_sorted_baggages = sorted(baggages, key=lambda x: x[0], reverse=True)
value_sorted_baggages = sorted(baggages, key=lambda x: x[1], reverse=True)

capacities = map(int, input().split())

for query in range(Q):
    L, R = map(int, input().split())
    no_box = L == 1 and R == M
    first_only = L == 2 and R == M
    last_only = L == 1 and R == M - 1
    one_box = first_only or last_only
    if no_box:
        print(0)
    elif one_box:
        print(value_sorted_baggages[0][1])
    else:
        available_boxes = baggages[:R] + baggages[L+1:]
        com = itertools.permutations(range(len(available_boxes)))
