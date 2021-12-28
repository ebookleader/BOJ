import sys

def func(N, lst, B, C):
    mainCnt, subCnt = N, 0
    # 총감독
    for i in range(N):
        lst[i] = lst[i] - B
    # 부감독
    for i in range(N):
        if lst[i] <= 0:
            continue
        x, y = divmod(lst[i], C)
        if y != 0:
            x += 1
        subCnt += x
    return mainCnt + subCnt
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

print(func(N, lst, B, C))