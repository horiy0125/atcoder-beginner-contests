target = int(input())
potential = input().split(" ")
min = int(potential[0])
max = int(potential[1])

can = []
for i in range(min,max+1):
  result = str(i/target)
  result = result.split(".")
  if result[1] == "0":
    can.append(i)
if len(can) != 0:
  print("OK")
else:
  print("NG")