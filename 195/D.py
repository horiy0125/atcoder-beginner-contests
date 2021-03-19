import itertools

N, M, Q = map(int, input().split())

baggages = []

for index in range(N):
    W, V = map(int, input().split())
    baggages.append([W, V])

value_sorted_baggages = sorted(baggages, key=lambda x: x[1], reverse=True)

capacities = list(map(int, input().split()))

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
        available_boxes = capacities[:R-1] + capacities[L+1:]
        available_boxes = sorted(available_boxes)
        value = 0
        for baggage in value_sorted_baggages:
            W, V = baggage[0], baggage[1]
            index = 0
            if available_boxes[index] >= W:
                value += V
            else:
                while available_boxes[index] < W:
                    index += 1

                value += V

            del available_boxes[index]

        print(value)
