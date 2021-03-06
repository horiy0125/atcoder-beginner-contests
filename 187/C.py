N = int(input())

words = {}
satisfiable = True

for i in range(N):
    new = input()
    if new[0] == '!':
        new = new[1:]
        if new in words and words[new] == '':
            satisfiable = False
            print(new)
            break
        else:
            words[new] = '!'
    else:
        if new in words and words[new] == '!':
            satisfiable = False
            print(new)
            break
        else:
            words[new] = ''

if satisfiable:
    print('satisfiable')
