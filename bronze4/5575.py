import sys
def calculateWorkingTime(lst) -> None:
    h = lst[3] - lst[0]
    m = lst[4] - lst[1]
    s = lst[5] - lst[2]
    if s < 0:
        s += 60
        m -= 1
    if m < 0:
        h -= 1
        m += 60
    print(h, m, s)

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
C = list(map(int, sys.stdin.readline().split()))
calculateWorkingTime(A)
calculateWorkingTime(B)
calculateWorkingTime(C)

