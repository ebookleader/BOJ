import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    lst = []
    for i in range(n):
        lst.append(list(map(int, sys.stdin.readline().split())))

    lst.sort(key = lambda x: x[0])  # 서류 성적순 오름차순 정렬
    res = 1
    rank = lst[0][1]
    for i in range(1, n):
        if lst[i][1] < rank:
            res += 1
            rank = lst[i][1]
    print(res)