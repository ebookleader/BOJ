import sys

def func(lst: list):
    res = 0
    if len(lst) % 2 == 0:   # 리스트의 길이가 짝수라면
        # 원소를 두개씩 곱해준다.
        for i in range(0, len(lst), 2):
            res += lst[i] * lst[i+1]
    else:   # 리스트의 길이가 홀수라면
        for i in range(0, len(lst)-1, 2):
            res += lst[i] * lst[i+1]
        res += lst[-1]
    return res

n = int(sys.stdin.readline())
positive, negative, one = [], [], []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x > 1:
        positive.append(x)
    elif x <= 0:
        negative.append(x)
    else:   # 1인경우
        one.append(x)
positive.sort(reverse=True) # 내림차순 정렬
negative.sort() # 오름차순 정렬

result = func(positive) + func(negative) + sum(one)
print(result)
# 혼자 푼 코드
# def func(n, lst: list):
#     res = []
#     i = (n - 1)
#     while i > 0:
#         n = lst[i]
#         if i > 0:
#             m = lst[i - 1]
#             mult = n * m
#             if (n == 0 and m < 0) or (n < 0 and m == 0):
#                 lst.pop()
#                 lst.pop()
#                 res.append(mult)
#                 i -= 1
#             elif mult > n:
#                 lst.pop()
#                 lst.pop()
#                 res.append(mult)
#                 i -= 1
#             else:
#                 lst.pop()
#                 res.append(n)
#         i -= 1
#     return sum(res + lst)
#
# n = int(sys.stdin.readline())
# number = []
# for _ in range(n):
#     number.append(int(sys.stdin.readline()))
#
# number.sort()   # 오름차순 정렬
# branch = 0
# for i in range(n):    # 음수&0 리스트는 내림차순 정렬
#     branch = i
#     if number[i] > 0:
#         break
# minusList = number[:branch]
# if branch > 0:
#     minusList.sort(reverse=True)
# plusList = number[branch:]
# x = func(len(plusList), plusList)
# y = func(len(minusList), minusList)
# print(x+y)