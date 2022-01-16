import sys

n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().rstrip()))

stack = []
remove_cnt = 0
for n in num:
    while stack and stack[-1] < n and remove_cnt < k:
        stack.pop()
        remove_cnt += 1
    stack.append(n)
print(''.join(map(str, stack[:len(num)-k])))
