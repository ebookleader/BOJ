import sys

n = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))
weight.sort()   # 오름차순 정렬

total = 1
for i in range(n):
    if total < weight[i]:
        break
    total += weight[i]
print(total)

# total = 0
# for i in range(n):
#     if total+1 < weight[i]:
#         break
#     total += weight[i]
# print(total+1)