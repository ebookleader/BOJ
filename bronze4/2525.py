import sys
A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline().rstrip())

B += C
if B > 59:
    A += (B//60)
    if A > 23:
        A -= 24
    B = (B%60)
print(f'{A} {B}')


