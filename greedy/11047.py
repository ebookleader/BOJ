import sys

def func(n, k, lst):
    result = 0
    i = (n-1)
    while i >= 0:
        if lst[i] <= k:
            a, b = divmod(k, lst[i])
            result += a
            k = b
        i -= 1
    print(result)

n, k = map(int, sys.stdin.readline().split())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))
func(n, k, lst)