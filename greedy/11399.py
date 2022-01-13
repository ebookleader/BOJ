import sys

def func(n, lst):
    lst.sort()
    result = 0
    for i in range(n, 0, -1):
        result = result + (i * lst[n - i])
    print(result)

n = int(sys.stdin.readline())
timeList = list(map(int, sys.stdin.readline().split()))
func(n, timeList)

