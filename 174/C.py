num = ""
ans = 0
count = 1

divide = int(input())
divided = divide / 2
divided = str(divided)
divided = divided.split(".")

if divided[1] == "0":
    print(-1)
else:
  while ans == 0:
    num += "7"
    Num = int(num)
    res = Num / divide
    res = str(res)
    res = res.split(".")
    if res[1] == "0":
        ans = count
        print(ans)
    else:
        count += 1
