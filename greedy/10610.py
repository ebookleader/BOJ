import sys

def func(n):
    lst = list(map(int, str(n)))
    lst.sort(reverse=True)
    if (sum(lst) % 3 != 0) or (0 not in lst):
        print(-1)
    else:
        print(''.join(map(str, lst)))
    return
N = int(sys.stdin.readline())
func(N)