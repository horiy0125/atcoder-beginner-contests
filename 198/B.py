N = str(input())
_N = N[::-1]

zero_count = 0

for i in range(len(N)):
    if _N[i] == '0':
        zero_count += 1
    else:
        break

n = f"{'0' * zero_count}{N}"
_n = n[::-1]

if n == _n:
    print('Yes')
else:
    print('No')
