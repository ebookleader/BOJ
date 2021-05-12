import sys
a, b, c, d = map(int, sys.stdin.readline().split())
ans1 = abs(a+b-(c+d))
ans2 = abs(a+c-(b+d))
ans3 = abs(a+d-(b+c))
print(min(ans1, ans2, ans3))