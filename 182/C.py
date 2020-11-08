import sys

N = int(input())

nums = [0] * 9

for digit in str(N):
    nums[int(digit) - 1] += 1

mod_one = nums[0] + nums[3] + nums[6]
mod_two = nums[1] + nums[4] + nums[7]
mod_three = nums[2] + nums[5] + nums[8]

judge = mod_one + (mod_two * 2) + (mod_three * 3)
delete = judge % 3

if delete == 0:
    print(0)
else:
    if judge < 3:
        print(-1)
    else:
        if delete == 1:
            if mod_one != 0:
                print(1)
            else:
                print(-1)
        else:
            if mod_two != 0:
                print(1)
                sys.exit()
            if mod_one >= 2:
                print(2)
            else:
                print(-1)
