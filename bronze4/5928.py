import sys
D, H, M = map(int, sys.stdin.readline().split())
ans1 = 11 * 24 * 60 + 11 * 60 + 11
ans2 = D * 24 * 60 + H * 60 + M
if (ans2 - ans1) < 0:
    print(-1)
else:
    print(ans2 - ans1)