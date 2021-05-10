import sys, math
L = int(sys.stdin.readline()) # 방학 총일
A = int(sys.stdin.readline()) # 국어 총페이지
B = int(sys.stdin.readline()) # 수학 총페이지
C = int(sys.stdin.readline()) # 하루 국어
D = int(sys.stdin.readline()) # 하루 수학
# Cx > A, Dx > B
x = math.ceil(A/C)
y = math.ceil(B/D)
print(L-max(x, y))