import sys

def makeTeam(N, M, K):
    result = 0
    while True:
        N -= 2
        M -= 1
        if (N >= 0) and (M >= 0) and (N+M) >= K:
            result += 1
        else:
            break
    return result

N, M, K = map(int, sys.stdin.readline().split())
print(makeTeam(N, M, K))
