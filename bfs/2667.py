import sys
from collections import deque

def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    visited[a][b] = True
    num = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if (0 <= xx < N) and (0 <= yy < N) and matrix[xx][yy] == 1 and visited[xx][yy] == False:
                queue.append([xx, yy])
                visited[xx][yy] = True
                num += 1
    return num

N = int(sys.stdin.readline())
matrix = []
visited = [[False] * N for _ in range(N)]
for _ in range(N):
    lst = list(map(int, sys.stdin.readline().rstrip()))
    matrix.append(lst)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
resList = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and not visited[i][j]:
            resList.append(bfs(i, j))
            cnt += 1
resList.sort()
print(cnt)
for res in resList:
    print(res)