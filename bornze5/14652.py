import sys
# N, M, K = map(int, sys.stdin.readline().split())
# n = K//M
# m = (K-M*n)%M
# print(f'{n} {m}')
n, m, k = map(int, sys.stdin.readline().split())
print(f'{k//m} {k%m}')