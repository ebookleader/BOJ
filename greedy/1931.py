import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(tuple(map(int, sys.stdin.readline().split())))

lst.sort(key=lambda x: (x[1], x[0]))

result = 1
end = lst[0][1]     # 가장 처음 회의의 종료시간
for i in range(1, n):
    if lst[i][0] >= end:
        result += 1
        end = lst[i][1]

print(result)

