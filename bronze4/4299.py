import sys
plus, diff = map(int, sys.stdin.readline().split())
x = (plus+diff) // 2
y = plus - x
if y >= 0 and (x+y == plus) and (x-y == diff):
    print(f'{x} {y}')
else:
    print(-1)