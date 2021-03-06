import math

X = int(input())

money = 100

past_year = 0

while money < X:
  past_year += 1
  money *= 1.01
  money = math.floor(money)

print(past_year)

# import math

# target = int(input())

# year = 0
# money = 100
# while money < target:
#   year += 1
#   money *= 1.01
#   money = math.floor(money)
# print(year)