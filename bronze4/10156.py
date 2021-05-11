import sys
k, n, m = map(int, sys.stdin.readline().split())
money = (k*n) - m
if money <= 0:
    print(0)
else:
    print(money)
