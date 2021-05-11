import sys
a, b, c = map(int, sys.stdin.readline().split())
lon = max(a, b, c)
lst = [a, b, c]
lst.remove(lon)
if lon ** 2 == lst[0] ** 2 + lst[1] ** 2:
    print(1)
elif a == b == c:
    print(2)
else:
    print(0)
