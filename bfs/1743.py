import sys
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    visited[x][y] = True
    cnt += 1
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if (0 < xx <= N) and (0 < yy <= M):
            if not visited[xx][yy] and matrix[xx][yy] == 1:
                cnt = dfs(xx, yy, cnt)
    return cnt


N, M, K = map(int, sys.stdin.readline().split())
matrix = [[0] * (M+1) for _ in range(N+1)]
visited = [[False] * (M+1) for _ in range(N+1)]

for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    matrix[r][c] = 1
maxi = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if not visited[i][j] and matrix[i][j] == 1:
            cnt = dfs(i, j, 0)
            if cnt > maxi:
                maxi = cnt
print(maxi)