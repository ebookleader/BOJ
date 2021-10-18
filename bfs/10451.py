import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    visited[x] = True
    nxt = (arr[x] - 1)
    if not visited[nxt]:
        dfs(nxt)

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    visited = [False] * N
    cnt = 0
    for i in range(N):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(cnt)