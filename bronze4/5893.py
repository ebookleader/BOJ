import sys
N = sys.stdin.readline().rstrip()
N = (int(N, 2) * 17)
print(bin(N)[2:])