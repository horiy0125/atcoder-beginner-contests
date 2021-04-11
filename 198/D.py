import sys

S1 = input()
S2 = input()
S3 = input()


def impossible():
    print('UNSOLVABLE')
    sys.exit()


if len(S1) > len(S3) or len(S2) > len(S3):
    impossible()
