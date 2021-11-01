import sys
from collections import deque

def bfs():
    global matrix, dx, dy
    queue = deque()
    zero = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                queue.append([i, j])
            elif matrix[i][j] == 0:
                zero += 1
    if zero == 0:
        print(0)
        return

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if (0 <= xx < n) and (0 <= yy < m) and matrix[xx][yy] == 0:
                queue.append([xx, yy])
                matrix[xx][yy] = matrix[x][y] + 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                print(-1)
                return
    print(max(map(max, matrix))-1)

m, n = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
bfs()
