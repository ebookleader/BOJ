import sys
from collections import deque

T = int(sys.stdin.readline())

visited = []
dd = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상 하 좌 우

def bfs(graph, i, j):
    checked = [[i, j]]
    queue = deque()
    queue.append([i, j])
    visited.append([i, j])

    while queue:
        x, y = queue.popleft()
        for d in dd:
            dx, dy = x+d[0], y+d[1]
            if (0 <= dx < N) and (0 <= dy < M):
                if graph[dx][dy] == 1 and [dx, dy] not in checked:
                    queue.append([dx, dy])
                    checked.append([dx, dy])
                    visited.append([dx, dy])
    return 1


for _ in range(T):
    visited = []
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for _ in range(N)] # 초기화
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    result = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and [i, j] not in visited:
                result += bfs(graph, i, j)
                if len(visited) == K:
                    break
    if len(visited) == K:
        print(result)