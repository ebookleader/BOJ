import sys
from math import ceil
k, w, m = map(int, sys.stdin.readline().split())
print(ceil((w-k)/m))