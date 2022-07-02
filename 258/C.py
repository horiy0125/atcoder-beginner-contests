N, Q = map(int, input().split())
S = input()

queries = []

for i in range(Q):
    query = input()
    t, n = query.split()
    queries.append([t, n])

count = 0
for query in queries:
    t = int(query[0])
    n = int(query[1])

    if t == 1:
        count += n
        if count >= N:
            count %= N
    else:
        index = n - count
        print(S[index-1])
