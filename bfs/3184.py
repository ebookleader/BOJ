import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
matrix = []
visited = [[0] * C for _ in range(R)]
sheep = wolf = 0
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상 하 좌 우

def bfs(x, y):
    global sheep, wolf
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    s, w = 0, 0
    if matrix[x][y] == 'v':
        w += 1
    elif matrix[x][y] == 'o':
        s += 1

    while queue:
        posX, posY = queue.popleft()

        for i in range(4):
            dx = posX + dir[i][0]
            dy = posY + dir[i][1]

            if (0 <= dx < R) and (0 <= dy < C):
                if visited[dx][dy] == 0 and matrix[dx][dy] != '#':
                    visited[dx][dy] = 1
                    queue.append([dx, dy])

                    if matrix[dx][dy] == 'v':
                        w += 1
                    elif matrix[dx][dy] == 'o':
                        s += 1
    if s > w:
        wolf -= w
    else:
        sheep -= s



for i in range(R):
    l = list(sys.stdin.readline().rstrip())
    matrix.append(l)
    for j in range(C):
        if l[j] == 'v':
            wolf += 1
        elif l[j] == 'o':
            sheep += 1

for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'v':
            bfs(i, j)

print(sheep, wolf)
