import sys
from collections import deque

def bfs(s):
    queue = deque()
    queue.append(s)
    while queue:
        l = queue.popleft()
        if l == K:
            return visited[l]
        for x in (l-1, l+1, 2*l):
            if (0 <= x <= 100001) and visited[x] == 0:
                visited[x] = visited[l] + 1
                queue.append(x)

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100002
if N >= K:
    print(N-K)
else:
    print(bfs(N))