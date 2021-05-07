import sys
arr = [0]*4
for i in range(4):
    arr[i] = int(sys.stdin.readline())
print(sum(arr)//60)
print(sum(arr)%60)