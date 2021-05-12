import sys
b1 = sys.stdin.readline().rstrip()
b2 = sys.stdin.readline().rstrip()
print(bin(int(b1, 2)*int(b2, 2))[2:])