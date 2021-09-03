import sys
from collections import deque

def bfs(s, t, cnt):
    queue = deque()
    queue.append([s, t, cnt]) # 태균, 상대
    while queue:
        me, opponent, cnt = queue.popleft()
        if me == opponent:
            return cnt
        if me < opponent:
            x, y = me*2, opponent+3
            if x <= y:
                queue.append([x, y, cnt + 1])
            x, y = me+1, opponent
            if x <= y:
                queue.append([x, y, cnt + 1])

C = int(sys.stdin.readline())
for _ in range(C):
    S, T = map(int, sys.stdin.readline().split())
    print(bfs(S, T, 0))