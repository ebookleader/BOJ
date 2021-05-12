import sys
A, B, C, D, E = [int(sys.stdin.readline()) for _ in range(5)]
ans = 0
if A < 0:
    ans += (abs(A) * C)
    ans += D
    A = 0
ans += (E * (B-A))
print(ans)