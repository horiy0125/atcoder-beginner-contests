data = input().split(" ")

five = data.count("5")
seven = data.count("7")

if five == 2 and seven == 1:
    print("YES")

else:
    print("NO")
