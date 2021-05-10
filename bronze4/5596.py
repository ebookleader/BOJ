import sys
minkook = list(map(int, sys.stdin.readline().split()))
manse = list(map(int, sys.stdin.readline().split()))
print(sum(minkook)) if sum(minkook) >= sum(manse) else print(sum(manse))
