N = int(input())

count = 0

for i in range(1, N+1):
    if not '7' in str(i):
        if not '7' in oct(i):
            count += 1

print(count)
