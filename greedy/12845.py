import sys

def func(n, lst):
    gold = (n-1) * max(lst)
    lst.remove(max(lst))
    for l in lst:
        gold += l
    print(gold)


n = int(sys.stdin.readline())
cardList = list(map(int, sys.stdin.readline().split()))
func(n, cardList)
