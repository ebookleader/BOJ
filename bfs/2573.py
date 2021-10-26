import sys, copy
from collections import deque

def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if (0 <= xx < N) and (0 <= yy < M) and tmpMatrix[xx][yy] > 0 and not visited[xx][yy]:
                queue.append([xx, yy])
                visited[xx][yy] = True

def melt(x, y):
    cnt = 0
    for k in range(4):
        xx = dx[k] + x
        yy = dy[k] + y
        if matrix[xx][yy] == 0:
            cnt += 1
    tmpMatrix[x][y] -= cnt
    if tmpMatrix[x][y] < 0:
        tmpMatrix[x][y] = 0

N, M = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
year = 0
flag = True

while flag:
    year += 1
    cnt = 0
    tmpMatrix = copy.deepcopy(matrix)
    visited = [[False] * M for _ in range(N)]

    for i in range(1, N-1):
        for j in range(1, M-1):
            if matrix[i][j] != 0:
                melt(i, j)
    for i in range(1, N-1):
        for j in range(1, M-1):
            if tmpMatrix[i][j] > 0 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    if cnt > 1:
        print(year)
        flag = False
    elif cnt == 0:
        print(0)
        flag = False
    else:
        matrix = tmpMatrix
