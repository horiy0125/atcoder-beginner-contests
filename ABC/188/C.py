N = int(input())

rates = input().split()


contestant = 2 ** N
point = int(contestant / 2)

for i in range(contestant):
    rates[i] = int(rates[i])

half1 = rates[:point]
half2 = rates[point:]

target = min([max(half1), max(half2)])

print(rates.index(target)+1)
