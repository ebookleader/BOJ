import sys

def dfs(num, p, cnt):
    sequence.append(num)
    lst = list(map(int, str(num)))
    res = 0
    for l in lst:
        res = res + (l ** p)
    if res not in sequence:
        dfs(res, p, cnt+1)
    else:
        sequence.append(res)
    return

A, P = map(int, sys.stdin.readline().split())
sequence = []
dfs(A, P, 0)
last = sequence[-1]
print(sequence.index(last))
