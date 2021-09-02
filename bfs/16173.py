import sys
from collections import deque

N = int( sys.stdin.readline())
graph = []

for i in range(N):
    l = list(map(int, sys.stdin.readline().split()))
    graph.append(l)

def bfs(graph, N):
    visited = [[0, 0]]
    queue = deque()
    queue.append([0, 0])

    while queue:
        cor = queue.popleft()
        x, y = cor[0], cor[1]
        step = graph[x][y]

        if step == -1:
            return True

        if x+step < N and ([x+step, y] not in visited):
            queue.append([x+step, y])
            visited.append([x+step, y])
        if y+step < N and ([x, y+step] not in visited):
            queue.append([x, y+step])
            visited.append([x, y+step])
    return False

print('HaruHaru') if bfs(graph, N) else print('Hing')