import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())
matrix = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = matrix[y][x] = 1

def dfs(start):
    visited[start] = True
    for i in range(1, N+1):
        if matrix[start][i] == 1 and not visited[i]:
            dfs(i)
    return

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
