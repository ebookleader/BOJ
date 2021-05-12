import sys
T = int(sys.stdin.readline())
ansList = list(map(int, sys.stdin.readline().split()))
ans = 0
for a in ansList:
    if a == T:
        ans += 1
print(ans)