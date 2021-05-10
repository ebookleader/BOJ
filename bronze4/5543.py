import sys
b1, b2, b3, cola, cider = [int(sys.stdin.readline()) for _ in range(5)]
print(min(b1, b2, b3) + min(cola, cider) - 50)