N, M, T = input().split()
N, M, T = int(N), int(M), int(T)

times = []

for i in range(M):
    start, end = input().split()
    start, end = int(start), int(end)

    if len(times) == 0:
        times.append(0)

    times.append(start)
    times.append(end)

times.append(T)

charge = False
batt = N
possible = True

for i in range(len(times) - 1):
    amount = times[i+1] - times[i]
    if charge:
        batt += amount
        charge = False
    else:
        batt -= amount
        charge = True

    if batt <= 0:
        possible = False
        break

    if batt > N:
        batt = N

if possible:
    print('Yes')
else:
    print('No')
