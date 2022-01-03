import sys

def function(h, w):
    if h == 1:
        print(1)
    elif h == 2:
        print(min(4, (w+1)//2))
    elif w < 7:
        print(min(4, w))
    else:
        print(5+(w-7))
    return

n, m = map(int, sys.stdin.readline().split())
function(n, m)