import sys
x, k = map(int, sys.stdin.readline().split())
if (7*k) <= x:
    print(k*7000)
elif (3.5*k) <= x:
    print(k*3500)
elif (1.75*k) <= x:
    print(k*1750)
else:
    print(0)