X = input()

if '.' in X:
    X = X.split('.')
    print(X[0])
else:
    print(int(X))
