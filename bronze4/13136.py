import sys
from math import ceil
h, w, n = map(int, sys.stdin.readline().split())
print(ceil(h/n) * ceil(w/n))