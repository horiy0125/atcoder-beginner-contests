import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

answer = 0

for b in B:
    a_index = bisect.bisect_left(A, b)
    c_index = bisect.bisect_right(C, b)

    a_num = a_index
    b_num = len(B) - c_index

    answer += a_num * b_num

print(answer)
