S = input()

numbers = []
able = False

if len(S) == 1:
    if int(S) == 8:
        able = True
elif len(S) == 2:
    pattern = [int(S), int(S[1] + S[0])]
    if pattern[0] % 8 == 0 or pattern[1] % 8 == 0:
        able = True
    else:
        able = False
else:
    for num in S:
        numbers.append(int(num))

    sums = []
    able = False

    for A in range(len(numbers)):
        for B in range(len(numbers)):
            if A != B:
                sums.append([A, B])

    for s in sums:
        for i in range(len(numbers)):
            if i not in s:
                summary = int(str(numbers[s[0]]) +
                              str(numbers[s[1]]) + str(numbers[i]))
                if summary % 2 == 0:
                    able = True
                if able == True:
                    break


if able == True:
    print('Yes')
else:
    print('No')
