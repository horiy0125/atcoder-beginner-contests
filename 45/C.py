import itertools

S = input()

length = len(S)
insert_plus = itertools.product([True, False], repeat=length - 1)

results = []

for i in insert_plus:
    nums = []
    stack = ''

    for n in range(length):
        stack += S[n]
        if n != length - 1:
            if i[n] == True:
                nums.append(int(stack))
                stack = ''
        else:
            nums.append(int(stack))

    results.append(sum(nums))

print(sum(results))
