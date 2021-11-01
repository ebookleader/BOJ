import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    visited = [False] * (n + 2)
    queue.append([x, y])
    visited[0] = True

    while queue:
        xx, yy = queue.popleft()
        if xx == rockX and yy == rockY:
            print("happy")
            return
        for i in range(1, n+2):
            dx, dy = coor[i][0], coor[i][1]
            dist = abs(dx - xx) + abs(dy - yy) # 현재 위치에서 다음 위치까지의 맨해튼 거리
            if dist <= 1000 and not visited[i]: # 20병 * 50m
                queue.append([dx, dy])
                visited[i] = True
    print("sad")

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline()) # 편의점 개수
    startX, startY = map(int, sys.stdin.readline().split())
    coor = []
    coor.append([startX, startY])
    for _ in range(n):
        coor.append(list(map(int, sys.stdin.readline().split())))
    rockX, rockY = map(int, sys.stdin.readline().split())
    coor.append([rockX, rockY])
    bfs(startX, startY)
