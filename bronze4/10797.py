import sys
day = int(sys.stdin.readline())
carList = list(map(int, sys.stdin.readline().split()))
ans = 0
for c in carList:
    if c == day:
        ans += 1
print(ans)