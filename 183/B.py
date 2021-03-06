data = input().split()

S = [int(data[0]), int(data[1])]
G = [int(data[2]), int(data[3])]

upper = (S[1] * G[0]) + (S[0] * G[1])
lower = S[1] + G[1]

print(upper / lower)