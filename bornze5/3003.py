import sys
arr = list(map(int, sys.stdin.readline().split()))
ansArr = [1,1,2,2,2,8]
for i in range(len(arr)):
    print(ansArr[i]-arr[i], end=' ')