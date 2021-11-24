import sys
from collections import deque

def bfs(n, k):
    global visited
    queue = deque()
    queue.append([n, 0])
    visited[n] = 0
    while queue:
        x, sec = queue.popleft()
        if x == k:
            print(sec)
            return
        next = [x+1, x-1, 2*x]
        for i in range(len(next)):
            if 0 <= next[i] <= 100000 and visited[next[i]] == -1:
                queue.append([next[i], sec+1])
                visited[next[i]] = x

n, k = map(int, sys.stdin.readline().split())
visited = [-1] * 100002
bfs(n, k)
tmp = k
ans = []
while tmp != n:
    ans.append(tmp)
    tmp = visited[tmp]
ans.append(n)
print(*(ans[::-1]))