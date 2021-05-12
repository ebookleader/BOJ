import sys
a, b = map(int, sys.stdin.readline().split())
rnd = 1
while True:
    if b*rnd - a*rnd >= b:
        break
    rnd += 1
print(rnd)

