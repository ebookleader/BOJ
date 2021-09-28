import sys
from collections import deque

n = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

matrix = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = matrix[y][x] = 1

visited = [0 for _ in range(n+1)]

def bfs(start, end):
    queue = deque()
    queue.append(start)
    visited[start] = 1 # 시작점

    while queue:
        node = queue.popleft()
        for i in range(len(matrix[node])):
            if matrix[node][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[node] + 1

    return -1 if visited[end] == 0 else (visited[end]-1)

print(bfs(start, end))

