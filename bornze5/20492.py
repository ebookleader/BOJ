import sys
N = int(sys.stdin.readline())
ans1 = int(N-(N*0.22))
ans2 = int(N-(N*0.2*0.22))
print(f'{ans1} {ans2}')