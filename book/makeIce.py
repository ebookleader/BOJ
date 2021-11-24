import sys
from collections import deque

def bfs(startX, startY):
    global visited, graph, dx, dy
    queue = deque()
    queue.append([startX, startY])
    visited[startX][startY] = True

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if (0 <= xx < N) and (0 <= yy < M):
                if graph[xx][yy] == 0 and not visited[xx][yy]:
                    queue.append([xx, yy])
                    visited[xx][yy] = True
    return

N, M = map(int, sys.stdin.readline().split())
graph = []
visited = [[False] * M for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            bfs(i, j)
            answer += 1
print(answer)