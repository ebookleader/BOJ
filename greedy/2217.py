import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort(reverse=True)

result = lst[0]
for i in range(1, len(lst)):
    tmp = lst[i] * (i+1)
    if tmp > result:
        result = tmp
print(result)
