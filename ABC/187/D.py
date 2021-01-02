N = int(input())

voters = []
tak = 0
ao = 0

for i in range(N):
    A, B = input().split()
    A, B = int(A), int(B)
    ao += A
    score = A * 2 + B
    voters.append([A, B, score])


sorted_vorters = sorted(voters, key=lambda x: x[2], reverse=True)
count = 0

for i in sorted_vorters:
    A = i[0]
    B = i[1]

    ao -= A
    tak += A + B
    count += 1

    if tak > ao:
        break

print(count)
