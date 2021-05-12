import sys
A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())
ans1 = A+D
ans2 = B+C
print(ans1) if ans1 < ans2 else print(ans2)