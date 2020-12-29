N = int(input())

X = []
Y = []

for index in range(N):
    x, y = input().split()
    X.append(int(x))
    Y.append(int(y))

if len(X) != len(set(X)):
    

# for index in range(N):
#     tilt = (dots[index + 1][1] - dots[index][1]) / \
#         (dots[index + 1][0] - dots[index][0])
#     tilts.append(tilt)

# print(tilts)
