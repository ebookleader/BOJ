import sys
# lst = list(map(int, sys.stdin.readline().split()))
# x1 = lst.pop(lst.index(min(lst)))
# x3 = lst.pop(lst.index(max(lst)))
# x2 = lst.pop()
# print(f'{x1} {x2} {x3}')

lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
for x in lst:
    print(x, end=' ')

