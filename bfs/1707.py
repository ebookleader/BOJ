import sys
from collections import deque

def bfs(x):
    queue = deque([x])
    visited[x] = 1 # 1 or -1로 체크
    while queue:
        node = queue.popleft()
        for k in matrix[node]:
            if visited[k] == 0: # 방문하지 않은 경우
                visited[k] = visited[node] * -1
                queue.append(k)
            else: # 방문한 정점일 경우
                if visited[k] == visited[node]:
                    return False
    return True

K = int(sys.stdin.readline())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    matrix = [[] * V for _ in range(V+1)]
    visited = [0] * (V+1)
    result = True
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        matrix[a].append(b)
        matrix[b].append(a)

    for i in range(1, V+1):
        if visited[i] == 0: # 방문하지 않은 정점에 대해 bfs 수행
            if not bfs(i): # 이분 그래프가 아닐 경우
                result = False
                break
    print("YES" if result else "NO")
