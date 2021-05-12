import sys
result = [sys.stdin.readline().rstrip() for _ in range(6)]
win = 0
for r in result:
    if r == 'W':
        win += 1
if win >= 5:
    print(1)
elif win >= 3:
    print(2)
elif win >= 1:
    print(3)
else:
    print(-1)