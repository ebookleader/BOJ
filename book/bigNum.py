import sys

def makeLargestNumb1(M, K, arr):
    answer = 0
    sortedArr = sorted(arr, reverse=True)  # 내림차순
    if sortedArr[0] == sortedArr[1]:
        answer = (sortedArr[0] * M)
    else:
        i, flag = 0, 0
        while i < M:
            if flag < K:
                answer += sortedArr[0]
                flag += 1
            else:
                answer += sortedArr[1]
                flag = 0
            i += 1
    return answer

N, M, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
print(makeLargestNumb1(M, K, arr))