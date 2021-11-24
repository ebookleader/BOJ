import sys
from collections import deque

def bfs(n, k):
    global visited
    queue = deque()
    queue.append(n)
    visited[n] = 0
    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[x])
            return
        next = [2*x, x-1, x+1]
        for i in range(len(next)):
            if 0 <= next[i] <= 100000 and visited[next[i]] == -1:
                queue.append(next[i])
                if i == 0:
                    visited[next[i]] = visited[x]
                else:
                    visited[next[i]] = visited[x] + 1

n, k = map(int, sys.stdin.readline().split())
visited = [-1] * 100002
bfs(n, k)