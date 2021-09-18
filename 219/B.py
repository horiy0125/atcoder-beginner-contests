S1 = input()
S2 = input()
S3 = input()
T = input()

answer = ''

for letter in T:
    if letter == '1':
        answer += S1
    elif letter == '2':
        answer += S2
    else:
        answer += S3

print(answer)
