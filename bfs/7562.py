import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append([nowX, nowY])
    visited[nowX][nowY] = 1
    while queue:
        x, y = queue.popleft()
        if x == targetX and y == targetY:
            print(visited[x][y]-1)
            return

        for i in range(8):
            xx = x + dx[i]
            yy = y + dy[i]
            if (0 <= xx < n) and (0 <= yy < n) and visited[xx][yy] == 0:
                queue.append([xx, yy])
                visited[xx][yy] = visited[x][y] + 1

T = int(sys.stdin.readline())
while T > 0:
    n = int(sys.stdin.readline())   # 한변의 길이
    nowX, nowY = map(int, sys.stdin.readline().split())
    targetX, targetY = map(int, sys.stdin.readline().split())
    visited = [[0] * n for _ in range(n)]
    dx = [-2, -2, 2, 2, -1, 1, -1, 1]
    dy = [-1, 1, -1, 1, -2, -2, 2, 2]
    bfs()
    T -= 1