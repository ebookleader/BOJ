import sys

# 입력
n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(sys.stdin.readline().rstrip())

# 식으로 바꾸어주기
dic = {}
for i in range(n):
    for j in range(len(lst[i])):
        x = int('1'+('0'*(len(lst[i])-j-1)))
        if lst[i][j] not in dic:
            dic[lst[i][j]] = x
        else:
            dic[lst[i][j]] += x

# 큰 값부터 차례대로 9, 8, ... 곱해주기
valueList = list(dic.values())
valueList.sort(reverse=True)
num, res = 9, 0
for v in valueList:
    res += (v * num)
    num -= 1
print(res)