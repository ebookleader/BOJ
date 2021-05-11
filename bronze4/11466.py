import sys
h, w = map(int, sys.stdin.readline().split())
if h < w:
    h, w = w, h
ans1, ans2 = 0, 0
ans1 = h/3 if h/3 <= w else w
ans2 = w/2
print(max(ans1, ans2))