import sys
from collections import deque

def bfs(graph, visited, startX, startY):
    global N, M
    queue = deque()
    queue.append([startX, startY])
    visited[startX][startY] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        if x == (N-1) and y == (M-1):
            print(visited[x][y])
            return
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if (0 <= xx < N) and (0 <= yy < M) and graph[xx][yy] == 1 and visited[xx][yy] == 0:
                queue.append([xx, yy])
                visited[xx][yy] = visited[x][y] + 1

N, M = map(int, sys.stdin.readline().split())
graph = []
visited = [[0] * M for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

bfs(graph, visited, 0, 0)