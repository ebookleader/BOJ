# 1: 2, 3: 6, 5: 12, 7: 20
# 2: 4, 4: 9, 6:16, 8: 25
import sys
n = int(sys.stdin.readline())
ans = 0
if (n % 2) == 0:
    ans = ((n // 2) + 1) ** 2
else:
    n += 1
    ans = ((n // 2)+1) ** 2
    ans -= ((n // 2) + 1)
print(ans)