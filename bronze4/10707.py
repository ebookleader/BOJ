import sys
A, B, C, D, P = [int(sys.stdin.readline()) for _ in range(5)]
X = A * P
Y = 0
if P <= C:
    Y = B
else:
    Y = B + D * (P - C)
print(min(X, Y))