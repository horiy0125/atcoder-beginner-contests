N = int(input())

if N == 1 and N == 2:
    answer = 2
elif N == 3:
    answer = 4
else:
    if N % 2 != 0:
        answer = 3
        divide = [N / 2 - 0.5, N / 2 + 0.5]
