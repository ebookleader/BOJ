import sys
from collections import deque

def bfs(x, y, n):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        tmpX, tmpY = queue.popleft()
        for k in range(4):
            xx = tmpX + dx[k]
            yy = tmpY + dy[k]
            if (0 <= xx < N) and (0 <= yy < N) and not visited[xx][yy] and matrix[xx][yy] > n:
                queue.append([xx, yy])
                visited[xx][yy] = True
    return

N = int(sys.stdin.readline())
matrix = []

for _ in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    matrix.append(lst)

maxi = 1
n = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while n <= 100:
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > n and not visited[i][j]:
                bfs(i, j, n)
                cnt += 1
    if maxi < cnt:
        maxi = cnt
    n += 1
print(maxi)