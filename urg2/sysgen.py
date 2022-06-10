from random import randint


def listpick(lst):
    lslen = len(lst)
    k = randint(0, lslen - 1)
    return lst[k]


overlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
runs = randint(30, 150)
for i in range(runs):
    ln = ''
    for k in range(3):
        ln += listpick(overlist)
    ln += '-'
    for k in range(3):
        ln += listpick(overlist)
    print(ln, end='  ')

