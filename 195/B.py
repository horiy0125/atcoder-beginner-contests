A, B, W = map(int, input().split())

W *= 1000

maximum = None
minimum = None

max_remain = W % B
if max_remain == 0:
    maximum = int(W / B)
else:
    max_reduce = B - max_remain
    reduce_per = max_reduce / int(W / B)

    if (B - reduce_per) < A:
        pass
    else:
        maximum = int(W / B) + 1

min_lack = W % B
if min_lack == 0:
    minimum = int(W / A)
else:
    not_enough = A - min_lack
    not_enough_per = not_enough / int(W / A)

    if (A + not_enough_per) > B:
        pass
    else:
        minimum = int(W / A)

if None in [maximum, minimum]:
    print("UNSATISFIABLE")
else:
    print(maximum, minimum)
