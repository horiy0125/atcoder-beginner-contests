N = int(input())
An = input().split()

for n in range(N):
    An[n] = int(An[n])


executable = True
count = 0

while executable:

    for an in An:
        if an % 2 == 1:
            executable = False
            break

    if executable:
        count += 1
        for n in range(N):
            An[n] /= 2

print(count)
