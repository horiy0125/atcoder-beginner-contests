import sys

N = input()

numbers = []

if len(N) == 1:
    print(0)
    sys.exit()
elif len(N) % 2 == 0:
    _N = N[:int(len(N) / 2)]
else:
    _N = '9' * int((len(N) - 1) / 2)

for n in range(int(_N)):
    n += 1
    numbers.append(int(f"{str(n)}{str(n)}"))

count = 0
for number in numbers:
    if number <= int(N):
        count += 1

print(count)
