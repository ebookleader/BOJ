import sys
n, area = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
num = n*area
for a in arr:
    print(a-num, end=' ')
