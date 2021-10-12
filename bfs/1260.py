import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
matrix = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = matrix[y][x] = 1

def dfs(matrix, start, visited = []):
    visited.append(start)
    for i in range(len(matrix[start])):
        if matrix[start][i] == 1 and (i not in visited):
            visited = dfs(matrix, i, visited)
    return visited

def bfs(matrix, start):
    visited = [start]
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for i in range(len(matrix[node])):
            if matrix[node][i] == 1 and (i not in visited):
                queue.append(i)
                visited.append(i)
    return visited

print(' '.join(map(str, dfs(matrix, V, []))))
print(' '.join(map(str, bfs(matrix, V))))


