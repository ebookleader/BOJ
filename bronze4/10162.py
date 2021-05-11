import sys
T = int(sys.stdin.readline())
# a 5분(300초), b 1분(60초), c 10초
a = T // 300
T = T % 300
b = T // 60
T = T % 60
c = T // 10
T = T % 10
if T == 0:
    print(a, b, c)
else:
    print(-1)
