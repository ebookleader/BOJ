import sys
from collections import deque

C = int(sys.stdin.readline())
N = int(sys.stdin.readline())

# 초기화
graph = {}
for i in range(1, C+1):
    graph[i] = []

# 연결 입력
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(graph, start):
    visited = [start]
    queue = deque([start])

    while queue:
        computer = queue.popleft()
        for c in graph[computer]:
            if c not in visited:
                visited.append(c)
                queue.append(c)
    return visited

print(len(bfs(graph, 1))-1)
