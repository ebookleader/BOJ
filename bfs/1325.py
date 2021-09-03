import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
connection = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    connection[b].append(a)

def bfs(start):
    visited = [0] * (N+1)
    visited[start] = 1
    queue = deque([start])
    n = 0
    while queue:
        computer = queue.popleft()
        for c in connection[computer]:
            if visited[c] == 0:
                n += 1
                visited[c] = 1
                queue.append(c)
    return n

maxi = 0
result = []
for i in range(1, N+1):
    if connection[i]:
        ans = bfs(i)
        if ans >= maxi:
            if ans > maxi:
                result = []
            result.append(i)
            maxi = ans
print(*result)