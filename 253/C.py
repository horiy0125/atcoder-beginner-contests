Q = int(input())

S = {}
nums = []

for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        try:
            S[query[1]] += 1
        except KeyError:
            S[query[1]] = 1
            nums.append(query[1])
    if query[0] == 2:
        try:
            S[query[1]] -= min([query[2], S[query[1]]])

            if S[query[1]] == 0:
                nums.remove(query[1])
        except KeyError:
            pass
    if query[0] == 3:
        print(max(nums) - min(nums))
