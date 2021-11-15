import sys
sys.setrecursionlimit(10 ** 7)

def solution(n, computers):
    answer = 0
    visited = [[False] * n for _ in range(n)]

    def dfs(i, j):
        visited[i][j] = True
        visited[j][i] = True
        for k in range(n):
            if computers[j][k] == 1 and not visited[j][k]:
                dfs(j, k)
        return

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                answer += 1
    return answer
