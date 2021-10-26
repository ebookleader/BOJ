import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append([S, 0])
    visited[S] = 0

    while queue:
        cur, cnt = queue.popleft()
        if cur == G:
            print(cnt)
            return
        up, down, nxt = cur+U, cur-D, cnt+1
        if 1 <= up <= F:
            if not visited[up]:
                visited[up] = nxt
                queue.append([up, nxt])
        if 1 <= down <= F:
            if not visited[down]:
                visited[down] = nxt
                queue.append([down, nxt])
    print("use the stairs")
    return

F, S, G, U, D = map(int, sys.stdin.readline().split())  # 총 층수, 현재위치, 목표위치, 위, 아래
visited = [False] * (F+1)
bfs()
