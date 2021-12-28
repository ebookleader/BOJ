import sys

N, K = map(int, sys.stdin.readline().split())
cnt = 0
while True:
    if N == 1:
        print(cnt)
        break
    if (N % K) == 0:
        N //= K
    else:
        N -= 1
    cnt += 1