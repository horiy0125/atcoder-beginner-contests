N = int(input())

exponentiation = 0
exponentiations = set()
a = 2

while a <= 1000000:
    b = 2
    while b <= 34:
        exponentiation = a ** b
        if exponentiation > N:
            break
        exponentiations.add(exponentiation)

        b += 1
    a += 1

print(N - len(exponentiations))
