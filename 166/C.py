N, M = input().split()
height = input().split()
able = []
for n in range(int(N)):
  able.append([])
for m in range(int(M)):
  con = input().split()
  con[0] = int(con[0]) - 1
  con[1] = int(con[1]) - 1
  able[con[0]].append(int(height[con[1]]))
  able[con[1]].append(int(height[con[0]]))
good = []
for n in range(int(N)):
  if len(able[n]) == 0:
    good.append(n)
  else:
    if int(height[n]) > max(able[n]):
      good.append(n)
print(len(good))