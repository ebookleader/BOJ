import sys
a, b, c, d = [int(sys.stdin.readline()) for _ in range(4)]
if (a == b) and (b == c) and (c == d):
    print('Fish At Constant Depth')
elif (a < b) and (b < c) and (c < d):
    print('Fish Rising')
elif (a > b) and (b > c) and (c > d):
    print('Fish Diving')
else:
    print('No Fish')