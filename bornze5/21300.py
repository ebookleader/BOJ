import sys
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
for a in arr:
    ans += (a*5)
print(ans)