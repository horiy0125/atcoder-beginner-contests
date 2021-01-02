A, B = input().split()

SA = 0
SB = 0

for i in A:
    SA += int(i)

for i in B:
    SB += int(i)

print(max([SA, SB]))
