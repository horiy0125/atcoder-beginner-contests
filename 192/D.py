
X = str(input())
M = int(input())

maximum = 0

for number in X:
    number = int(number)
    if number > maximum:
        maximum = number

initial = maximum + 1
sysnums = []
answer = 0

for i in range(maximum+1, 11):
    sysnums.append(i)

while True:
    split_num = int(len(sysnums) / 2)
    firsts = sysnums[:split_num]
    lasts = sysnums[split_num:]

    first = 0
    last = 0

    index = len(X) - 1
    for x in X:
        first += int(x) * (firsts[len(firsts) - 1] ** index)
        index -= 1

    index = len(X) - 1
    for x in X:
        last += int(x) * (lasts[len(firsts) - 1] ** index)
        index -= 1

    if last <= M:

        # index = len(X) - 1
        # latest = 0
        # count = 0
        # sysnum = maximum + 1
        # while True:
        #     number = 0
        #     for x in X:
        #         number += int(x) * (sysnum ** index)
        #         index -= 1

        #     index = len(X) - 1
        #     sysnum += 1

        #     if number <= M:
        #         count += 1
        #         if number == M:
        #             break
        #     else:
        #         break

        # print(count)
