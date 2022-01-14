import sys

def func(lst):
    profit = 0
    maxi = 0
    for i in range(len(lst)-1, -1, -1):
        if lst[i] >= maxi:
            maxi = lst[i]
        else:
            profit += (maxi - lst[i])
    print(profit)

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    priceList = list(map(int, sys.stdin.readline().split()))
    func(priceList)