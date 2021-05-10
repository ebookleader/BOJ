import sys, math
diagonal, hr, wr = map(int, sys.stdin.readline().split())
dr = math.sqrt(hr**2 + wr**2)
height = (hr*diagonal) / dr
weight = (wr*diagonal) / dr
print(f'{int(height)} {int(weight)}')