N, K = input().split()

sunuke = []
for n in range(int(N)):
  sunuke.append([])
for k in range(int(K)):
  people = input()
  no = input().split()
  for i in no:
    sunuke[int(i)-1].append(int(K))
target = []
for i in range(int(N)):
  if len(sunuke[i]) == 0:
    target.append(i)
print(len(target))