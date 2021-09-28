import sys
sys.setrecursionlimit(2500)

d = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, 1], [1, -1]] # 상하좌우 대각선 8방향

def dfs(x, y):
    visited[x][y] = True
    for i in range(8):
        dx = x + d[i][0]
        dy = y + d[i][1]

        if (0 <= dx < h) and (0 <= dy < w):
            if board[dx][dy] == '1' and not visited[dx][dy]:
                dfs(dx, dy)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    board = []
    visited = [[False] * w for _ in range(h)]
    cnt = 0
    for _ in range(h):
        board.append(list(sys.stdin.readline().rstrip().split()))
    for i in range(h):
        for j in range(w):
            if board[i][j] == '1' and not visited[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)