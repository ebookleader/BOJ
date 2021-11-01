import sys
from collections import deque

def bfs(now):
    global visited, time
    queue = deque()
    queue.append(now)
    time[now] = 0
    visited[now] = 1

    while queue:
        x = queue.popleft()
        for l in (x+1, x-1, 2*x):
            if 0 <= l <= 100000:
                if time[l] == -1:   # 처음 방문
                    queue.append(l)
                    time[l] = time[x] + 1
                    visited[l] = visited[x]
                elif time[l] == time[x] + 1:    # 처음방문이 아니고 최단시간 방문이라면
                    visited[l] += visited[x]    # 경로의 수 갱신

n, k = map(int, sys.stdin.readline().split())
time = [-1] * 100001    # 걸린시간
visited = [0] * 100001  # 경로의 수
bfs(n)
print(time[k])
print(visited[k])