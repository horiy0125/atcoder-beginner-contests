C = input()

C1 = C[0]
C2 = C[1]
C3 = C[2]

if C1 == C2 and C2 == C3:
    if C3 == C1:
        print("Won")
else:
    print("Lost")
