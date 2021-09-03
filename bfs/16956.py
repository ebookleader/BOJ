import sys

R, C = map(int, sys.stdin.readline().split())
graph = []
for _ in range(R):
    l = list(sys.stdin.readline().rstrip())
    graph.append(l)

d = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우 이동

def bfs(i, j):
    # 상하좌우 조사
    for k in range(4):
        dx = i + d[k][0] # 이동한 x좌표
        dy = j + d[k][1] # 이동환 y좌표
        if (0 <= dx < R) and (0 <= dy < C):
            if graph[dx][dy] == 'S': # 주변에 양이 있는 경우
                return False
            elif graph[dx][dy] == '.':
                graph[dx][dy] = 'D'
    return True


for i in range(R):
    for j in range(C):
        flag = True
        if graph[i][j] == 'W': # 늑대인경우
            flag = bfs(i, j)
            if not flag:
                print(0)
                break

if flag:
    print(1)
    for lst in graph:
        print(''.join(lst))