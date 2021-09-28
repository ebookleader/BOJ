import sys
from collections import deque

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(startX, startY, board, visited):
    queue = deque() # x좌표, y좌표, 이동거리
    queue.append([startX, startY])
    visited[startX][startY] = 1

    while queue:
        x, y = queue.popleft()
        if x == (N-1) and y == (M-1):
            return visited[x][y]
        for i in range(4):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if (0 <= dx < N) and (0 <= dy < M):
                if board[dx][dy] == '1' and visited[dx][dy] == 0:
                    visited[dx][dy] = visited[x][y] + 1
                    queue.append([dx, dy])

N, M = map(int, sys.stdin.readline().split())
board = []
visited = [[0] * M for _ in range(N)]
for _ in range(N):
    lst = list(sys.stdin.readline().rstrip())
    board.append(lst)

print(bfs(0, 0, board, visited))

