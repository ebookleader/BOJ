import sys
line = sys.stdin.readline().rstrip()
print('YES') if int(line[0]) + int(line[4]) == int(line[-1]) else print('NO')