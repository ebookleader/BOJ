import sys

def choiceLargestNum(board):
    minArr = []
    for lst in board:
        minArr.append(min(lst))
    return max(minArr)

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
print(choiceLargestNum(board))
