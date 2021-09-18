import sys

X = int(input())


if X >= 90:
    print('expert')
    sys.exit()
else:
    if X >= 70:
        print(90 - X)
        sys.exit()
    if X >= 40:
        print(70 - X)
        sys.exit()
    else:
        print(40 - X)
        sys.exit()
