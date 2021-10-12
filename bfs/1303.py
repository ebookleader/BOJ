import sys

N, M = map(int, sys.stdin.readline().split())
matrix = []
visited = [[False] * N for _ in range(M)]
for _ in range(M):
    lst = list(sys.stdin.readline().rstrip())
    matrix.append(lst)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt, team):
    visited[x][y] = True
    cnt += 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if (0 <= xx < M) and (0 <= yy < N) and not visited[xx][yy] and matrix[xx][yy] == team:
            cnt = dfs(xx, yy, cnt, team)
    return cnt

def calculateForce(team):
    result = tmp = 0
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == team and not visited[i][j]:
                tmp = dfs(i, j, 0, team)
                result = result + (tmp ** 2)
    return result

print(calculateForce('W'), calculateForce('B'))
