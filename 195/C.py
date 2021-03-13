N = int(input())

digits = len(str(N))

answer = 0

repeat = int(digits / 3)
if digits % 3 == 0:
    repeat -= 1

for index in range(repeat):
    number = N - int('999' * (index + 1))
    answer += number

print(answer)
