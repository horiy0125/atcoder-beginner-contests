N = int(input())

person = []

for n in range(N):
    ai, bi = map(int, input().split())

    person.append([ai, bi])

time = []

for a in range(N):
    for b in range(N):

        if a == b:
            time.append(person[a][0] + person[a][1])
        else:
            A = person[a][0]
            B = person[b][1]

            time.append(max([A, B]))

print(min(time))
