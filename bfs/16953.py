import sys
from collections import deque

def bfs():
    global a, b
    queue = deque()
    queue.append([a, 0])

    while queue:
        x, cnt = queue.popleft()
        if x == b:
            print(cnt+1)
            return
        if x*2 <= b:
            queue.append([x*2, cnt+1])
        tmp = int(str(x)+'1')
        if tmp <= b:
            queue.append([tmp, cnt+1])
    print(-1)

a, b = map(int, sys.stdin.readline().split())
bfs()