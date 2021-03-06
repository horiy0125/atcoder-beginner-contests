S = input()

able = False
numbers = [0] * 10

if len(S) == 1:
    if S == '8':
        able = True
elif len(S) == 2:
    patterns = [int(S), int(S[1] + S[0])]
    if (patterns[0] % 8 == 0 or patterns[1] % 8 == 0):
        able = True
else:
    for number in S:
        numbers[int(number)] += 1

    eights = []
    eight = 104
    while eight < 1000:
        if not '0' in str(eight):
            eights.append(eight)
        eight += 8

    for eight in eights:
        conditions = [
            numbers[int(str(eight)[0])] != 0,
            numbers[int(str(eight)[1])] != 0,
            numbers[int(str(eight)[2])] != 0,
        ]
        if not False in conditions:
            able = True

if able:
    print('Yes')
else:
    print('No')
