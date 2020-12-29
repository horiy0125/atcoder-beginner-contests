N = int(input())

array = input().split()

for i in range(N):
    array[i] = int(array[i])

array.sort()

answer = 0

for i in range(N):
    num = array[i]
    time = N - 1
    minus_time = N - i - 1
    result = num * (time - minus_time * 2)
    answer += result

print(answer)
