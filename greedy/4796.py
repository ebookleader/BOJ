import sys

cnt = 1
while True:
    L, P, V = (map(int, sys.stdin.readline().split()))
    if L == P == V == 0:
        break
    else:
        result = 0
        x, y = divmod(V, P)
        result += (x * L)
        if L < y:
            result += L
        else:
            result += y
    print("Case "+str(cnt)+": "+str(result))
    cnt += 1