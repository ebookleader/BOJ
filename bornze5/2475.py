import sys
arr = list(map(int, sys.stdin.readline().split()))
s = 0
for a in arr:
    s += (a**2)
print(s%10)