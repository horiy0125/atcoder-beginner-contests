import itertools

S = input()

absolute_nums = []
maybe_nums = []

count = 0

for letter in S:
    if letter == 'o':
        absolute_nums.append(count)
    elif letter == '?':
        maybe_nums.append(count)

    count += 1

l_a = len(absolute_nums)
l_m = len(maybe_nums)


if l_a > 4:
    print(0)

elif l_a == 4:
    print(24)

elif l_a == 0 and l_m == 0:
    print(0)

else:
    if l_m == 0:
        fill_nums = list(itertools.combinations_with_replacement(
            absolute_nums, 4 - l_a))

    else:
        fill_nums = list(itertools.combinations_with_replacement(
            absolute_nums + maybe_nums, 4 - l_a))

    numbers = []

    for case in fill_nums:
        number = absolute_nums + list(case)
        numbers.append(number)

    pins = set()

    for case in numbers:
        number = set(itertools.permutations(case, 4))
        pins = pins | number

    print(len(pins))
