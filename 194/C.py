N = int(input())
A = input().split()

number_appear = dict()

for i in range(-200, 201):
    number_appear[str(i)] = 0

for i in range(len(A)):
    number_appear[A[i]] += 1

answer = 0

for i in range(-200, 201):
    for j in range(-200, 201):
        if i == j:
            pass
        else:
            square = (i - j) ** 2
            answer += square * number_appear[str(i)] * number_appear[str(j)]

print(int(answer / 2))
