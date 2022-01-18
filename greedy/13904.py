import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort(reverse=True, key=lambda x: x[1])
assign = {}
for day, score in lst:
    if day in assign:
        for i in range(day, 0, -1):
            if i not in assign:
                assign[i] = score
                break
    else:
        assign[day] = score
print(sum(assign.values()))