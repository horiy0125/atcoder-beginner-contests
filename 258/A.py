K = int(input())

if K >= 60:
    h = 22
    m = K - 60
else:
    h = 21
    m = K

if m < 10:
    m = f"0{m}"

print(f"{h}:{m}")
